#!/usr/bin/python3
# -*- coding: future_fstrings -*-
import importlib
import logging
import sys
import tempfile



from asp.asp_util import program2primal
from common import *
from dpdb.abstraction import MinorGraph, ClingoControl
from dpdb.db import BlockingThreadedConnectionPool, DBAdmin, DEBUG_SQL, setup_debug_sql
from dpdb.problems.nestpmc import NestPmc
from dpdb.problems.sat_util import *

from dpdb.writer import FileWriter
from tool import clingoext
from tool.groundprogram import ClingoRule, ClingoProject

logger = logging.getLogger("nestHDB")
# setup_logging("DEBUG")
# setup_logging()
setup_debug_sql()


class AppConfig(object):
    """
    Class for application specific options.
    """

    def __init__(self):
        self.eclingo_verbose = 1


def _read(path):
    if path == "-":
        return sys.stdin.read().replace("show", "project")
    with open(path) as file_:
        return file_.read().replace("show", "project")


class Application(object):
    """
    Application class that can be used with `clingo.clingo_main` to solve CSP
    problems.
    """

    def __init__(self, path):
        self._project = set()
        self._program = []
        self._rule = []
        self._atom = set()
        self._atomToVertex = {}
        self._vertexToAtom = {}
        self.control = clingoext.Control()
        self.program_name = "clingoext"
        self.version = "5.5.0"
        self.config = AppConfig()
        self._weights = {}
        self.control.add("base", [], _read(path))

    def ground(self):
        self.control.ground()
        logger.info("------------------------------------------------------------")
        logger.info("   Grounded Program")
        logger.info("------------------------------------------------------------")
       # logger.info(self.control.ground_program.objects)
       # logger.info("------------------------------------------------------------")

    def generate_rule(self):
        self._max = 1
        i = self._max
        for o in self.control.ground_program.objects:
           # print(o)
            if isinstance(o, ClingoProject):
                self._project.update(o.atoms)
            if isinstance(o, ClingoRule):
                o.atoms = set(o.head)
                o.atoms.update(tuple(map(abs, o.body)))
                self._program.append(o)
                #      self._unary.update(o.atoms)
                if len(o.atoms) >= 1 and not o.choice:
                    # added head is empty to disable condition that body should be > 1
                    # this one for generating cliques and ground rule to collect nodes .

                    atom_in_head = frozenset(o.head)
                    atom_in_body = frozenset(o.body)
                    temp = [atom_in_head, atom_in_body]
                    for a in o.atoms.difference(self._atomToVertex):
                        # add mapping for atom not yet mapped
                        self._atomToVertex[a] = i
                        self._vertexToAtom[i] = a
                        self._atom.add(a)
                        self._max = i
                        i += 1
                    self._rule.append(temp)
       # print(self._rule)
    def get_program(self):
        return self._atom, self._rule, self._project


class Program:
    def __init__(self, atoms, rules, projected=None):
        self.atoms = atoms
        self.num_atoms = len(atoms)
        self.rules = rules
        self.num_rules = len(rules)
        self.projected = projected
        self.atoms_rules_dict = defaultdict(set)


class Graph:
    def __init__(self, nodes, edges, adj_list):
        self.nodes = nodes
        self.edges = edges
        self.adj_list = adj_list
        self.tree_decomp = None

    @property
    def num_nodes(self):
        return len(self.nodes)

    @property
    def num_edges(self):
        return len(self.edges)

    def abstract(self, non_nested):
       # print(non_nested)
        proj_out = self.nodes - non_nested
        mg = MinorGraph(self.nodes, self.adj_list, proj_out)
        mg.abstract()
        mg.add_cliques()
        self.nodes = mg.nodes
        self.edges = mg.edges
        self.adj_list = mg.adj_list
        self.mg = mg

    def normalize(self):
        self.nodes_normalized = set()
        self.edges_normalized = set()
        self.adj_list_normalized = {}
        self._node_map = {}
        self._node_rev_map = {}

        last = 0
        for n in self.nodes:
            last += 1
            self._node_map[n] = last
            self._node_rev_map[last] = n
            self.nodes_normalized.add(last)

        for e in self.edges:
            u = self._node_map[e[0]]
            v = self._node_map[e[1]]
            if u < v:
                self.edges_normalized.add((u, v))
            else:
                self.edges_normalized.add((v, u))

    def decompose(self, **kwargs):
        global cfg
        self.normalize()
        self.tree_decomp = decompose(self.num_nodes, self.edges_normalized, cfg["htd"], node_map=self._node_rev_map,
                                     minor_graph=self.mg, **kwargs)


interrupted = False
cache = {}


class Problem:
    def __init__(self, program, non_nested, depth=0, **kwargs):
        self.program = program
        self.projected = program.projected
        self.projected_orig = set(program.projected)
        self.non_nested = non_nested
        self.non_nested_orig = non_nested
        self.maybe_sat = True
        self.models = None
        self.depth = depth
        self.kwargs = kwargs
        self.sub_problems = set()
        self.nested_problem = None
        self.active_process = None



    def decompose_nested_primal(self):
        num_vars, edges, adj = program2primal(self.program.num_atoms, self.program.rules, self.program.atoms_rules_dict,
                                          True)
        self.graph = Graph(set(self.program.atoms), edges, adj)
        logger.info(f"Primal graph #vertices: {num_vars}, #edges: {len(edges)}")
        self.graph.abstract(self.non_nested)
        logger.info(f"Nested primal graph #vertices: {self.graph.num_nodes}, #edges: {self.graph.num_edges}")
        self.graph.decompose(**self.kwargs)

    def choose_subset(self):
        global cfg
        cfg_asp = cfg["nesthdb"]["asp"]
        for enc in cfg_asp["encodings"]:
            if interrupted:
                return
            size = enc["size"]
            timeout = 30 if "timeout" not in enc else enc["timeout"]
            logger.debug("Running clingo %s for size %d and timeout %d", enc["file"], size, timeout)
            c = ClingoControl(self.graph.edges, self.non_nested)
            res = c.choose_subset(min(size, len(self.non_nested)), enc["file"], timeout)[2]
            if len(res) == 0:
                logger.warning(
                    "Clingo did not produce an answer set, fallback to previous result {}".format(self.non_nested))
            else:
                self.non_nested = set(res[0])
            logger.debug("Clingo done%s", " (timeout)" if c.timeout else "")
        assert (len(self.non_nested) > 0)

    def call_solver(self, type):
        global cfg, solver_parser_cls, solver_parser

        logger.info(
            f"Call solver: {type} with #atoms {self.program.num_atoms}, #rules {len(self.program.rules)}, #projected {len(self.projected)}")

        cfg_str = f"{type}_solver"
        assert (cfg_str in cfg["nesthdb"])
        assert ("path" in cfg["nesthdb"][cfg_str])
        local_cfg = cfg["nesthdb"][cfg_str]
        solver = [local_cfg["path"]]

        if "seed_arg" in local_cfg:
            solver.append(local_cfg["seed_arg"])
            solver.append(str(self.kwargs["runid"]))
        if "args" in local_cfg:
            solver.extend(local_cfg["args"].split(' '))
        if "output_parser" in local_cfg:
            solver_parser = local_cfg["output_parser"]
            reader_module = importlib.import_module("dpdb.reader")
            solver_parser_cls = getattr(reader_module, solver_parser["class"])

        tmp = tempfile.NamedTemporaryFile().name

        with FileWriter(tmp) as fw:

            fw.write_program(self.program.rules, projected_atoms=self.projected)
            for i in range(0, 128, 1):
                if interrupted:
                    return -1

                self.active_process = psat = subprocess.Popen(solver + [tmp], stdout=subprocess.PIPE)
                output = solver_parser_cls.from_stream(psat.stdout,**solver_parser["args"])
                psat.wait()
                psat.stdout.close()
                self.active_process = None
                if interrupted:
                    return -1
                result = int(getattr(output, solver_parser["result"]))
                if psat.returncode == 245 or psat.returncode == 250:
                    logger.debug("Retrying call to external solver, returncode {}, index {}".format(psat.returncode, i))
                else:
                    logger.debug("No Retry, returncode {}, result {}, index {}".format(psat.returncode, result, i))
                    break

        logger.info(f"Solver {type} result: {result}")
        return result

    def solve_classic(self):
        if interrupted:
            return -1
        # uncomment the following line for sharpsat solving
        # return self.call_solver("sharpsat")
        return self.call_solver("clingo")
    #    if self.program.atoms == self.projected:
    #        return self.call_solver("sharpsat")
     #   else:
       #     return self.call_solver("pmc")

    def final_result(self, result):
        len_old = len(self.projected_orig)
        len_new = len(self.projected)
        len_diff = len_old - len_new
        exp = 2 ** len_diff
        final = result * exp
        if not self.kwargs["no_cache"]:
            frozen_rules = frozenset([frozenset(c) for c in self.program.rules])
            cache[frozen_rules] = final
        return final

    def get_cached(self):
        #print(self.program.rules)
        frozen_rules = frozenset([frozenset(c) for c in self.program.rules])
        if frozen_rules in cache:
            return cache[frozen_rules]
        else:
            return None

    def nestedpmc(self):
        global cfg

        pool = BlockingThreadedConnectionPool(1, cfg["db"]["max_connections"], **cfg["db"]["dsn"])
        problem_cfg = {}
        if "problem_specific" in cfg and "nestpmc" in cfg["problem_specific"]:
            problem_cfg = cfg["problem_specific"]["nestpmc"]
        if interrupted:
            return -1
        self.nested_problem = NestPmc("test", pool, **cfg["dpdb"],
                                      **flatten_cfg(problem_cfg, [], '_', NestPmc.keep_cfg()), **self.kwargs)
        if interrupted:
            return -1
        self.nested_problem.set_td(self.graph.tree_decomp)
        if interrupted:
            return -1
        self.nested_problem.set_recursive(self.solve_rec, self.depth)
        if interrupted:
            return -1
        self.nested_problem.set_input(self.graph.num_nodes, -1, self.projected, self.non_nested_orig,
                                      self.program.atoms_rules_dict)
        if interrupted:
            return -1
        self.nested_problem.setup()
        if interrupted:
            return -1
        self.nested_problem.solve()
        if interrupted:
            return -1
        return self.nested_problem.model_count

    def solve(self):
        logger.info(
            f"Original #atoms: {self.program.num_atoms}, #rules: {self.program.num_rules}, #projected: {len(self.projected_orig)}, depth: {self.depth}")
        # self.preprocess()
      #  if not self.maybe_sat:
       #     logger.info("Preprocessor UNSAT")
        #    return 0
        #if self.models is not None:
         #   logger.info(f"Solved by preprocessor: {self.models} models")
          #  return self.final_result(self.models)

        self.non_nested = self.non_nested.intersection(self.projected)
        logger.info(
            f"Preprocessing #atoms: {self.program.num_atoms}, #rules: {self.program.num_rules}, #projected: {len(self.projected)}")

        if not self.kwargs["no_cache"]:
            cached = self.get_cached()
            if cached != None:
                logger.info(f"Cache hit: {cached}")
                return cached


        if len(self.projected.intersection(self.program.atoms)) == 0:
            logger.info("Intersection of atoms and projected is empty")
            return self.final_result(self.solve_classic())

        if self.depth >= cfg["nesthdb"]["max_recursion_depth"]:
            return self.final_result(self.solve_classic())


        self.decompose_nested_primal()

        if interrupted:
            return -1

        if self.depth > 0 and self.graph.tree_decomp.tree_width >= cfg["nesthdb"][
            "threshold_hybrid"]:  # TODO OR PROJECTION SIZE BELOW TRESHOLD OR CLAUSE SIZE BELOW TRESHOLD
            logger.info("Tree width >= hybrid threshold ({})".format(cfg["nesthdb"]["threshold_hybrid"]))
            return self.final_result(self.solve_classic())

        if self.graph.tree_decomp.tree_width >= cfg["nesthdb"]["threshold_abstract"]:
            logger.info("Tree width >= abstract threshold ({})".format(cfg["nesthdb"]["threshold_abstract"]))
            self.choose_subset()
            logger.info(f"Subset #non-nested: {len(self.non_nested)}")
            self.decompose_nested_primal()
            if self.graph.tree_decomp.tree_width >= cfg["nesthdb"]["threshold_abstract"]:
                logger.info("Tree width after abstraction >= abstract threshold ({})".format(
                    cfg["nesthdb"]["threshold_abstract"]))
                return self.final_result(self.solve_classic())

        return self.final_result(self.nestedpmc())

    def solve_rec(self, atoms, rules, non_nested, projected, depth=0, **kwargs):
        if interrupted:
            return -1

        p = Problem(Program(atoms, rules, projected), non_nested, depth, **kwargs)
        self.sub_problems.add(p)
        result = p.solve()
        self.sub_problems.remove(p)
        return result

    def interrupt(self):
        logger.warning("Problem interrupted")
        interrupted = True
        if self.nested_problem != None:
            self.nested_problem.interrupt()
        for p in list(self.sub_problems):
            p.interrupt()
        if self.active_process != None:
            if self.active_process.poll() is None:
                self.active_process.send_signal(signal.SIGTERM)


def main():
    global cfg
    arg_parser = setup_arg_parser("%(prog)s [general options] -f input-file")
    arg_parser.add_argument("--no-cache", dest="no_cache", help="Disable cache", action="store_true")
    args = parse_args(arg_parser)
    cfg = read_cfg(args.config)

    file_path = args.file

    Decomposer = Application(file_path)
    Decomposer.ground()
    Decomposer.generate_rule()
    output = Decomposer.get_program()
    program = Program(output[0],output[1],output[2])
    problem = Problem(program,program.atoms,**vars(args))

    def signal_handler(sig, frame):
        if sig == signal.SIGUSR1:
            logger.warning("Terminating because of error in worker thread")
        else:
            logger.warning("Killing all connections")
        problem.interrupt()
        app_name = None
        if "application_name" in cfg["db"]["dsn"]:
            app_name = cfg["db"]["dsn"]["application_name"]
        admin_db.killall(app_name)

    admin_db = DBAdmin.from_cfg(cfg["db_admin"])
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGUSR1, signal_handler)


    result = problem.solve()
    logger.info(f"PMC: {result}")


if __name__ == "__main__":
    main()
