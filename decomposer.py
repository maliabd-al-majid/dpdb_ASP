"""
Main module providing the application logic.
"""
import logging
import os
import signal
import subprocess
import sys

from dpdb.db import BlockingThreadedConnectionPool, setup_debug_sql, DBAdmin
# set library path
from dpdb.problems import SharpSat
from dpdb.reader import TdReader
from dpdb.treedecomp import TreeDecomp
# from dpdb.writer import StreamWriter
from asp.cyclicGraph import Graph
from htd_validate.utils import hypergraph
# import tool.clingoext
from tool import clingoext
from tool.clingoext import ClingoRule

# from htd_validate.decompositions import *


# from dpdb.problems.sat_util import *
from asp.asp_util import get_positive_value, get_rule_loop, read_cfg, get_rule_No_loop

logger = logging.getLogger("asp2sat")
logging.basicConfig(format='[%(levelname)s] %(name)s: %(message)s', level="INFO")


class AppConfig(object):
    """
    Class for application specific options.
    """

    def __init__(self):
        self.eclingo_verbose = 0


class Application(object):
    """
    Application class that can be used with `clingo.clingo_main` to solve CSP
    problems.
    """

    def __init__(self):
        self.program_name = "clingoext"
        self.version = "5.5.0"
        self.config = AppConfig()
        self._weights = {}

    def _read(self, path):
        if path == "-":
            return sys.stdin.read()
        with open(path) as file_:
            return file_.read()

    def primalGraph(self):
        return self._graph

    def _generateRule(self):
        self._program = []
        self._rule = []
        self._atomToVertex = {}
        self._max = 1
        self._unary = set()
        i = self._max
        for o in self.control.ground_program.objects:

            if isinstance(o, ClingoRule):

                o.atoms = set(o.head)
                o.atoms.update(tuple(map(abs, o.body)))
                self._program.append(o)
                if len(o.atoms) > 1 or len(o.head) == 0:
                    # added head is empty to disable condition that body should be > 1
                    # this one for generating cliques and ground rule to collect nodes .

                    atom_in_head = set(o.head)
                    atom_in_body = set(o.body)
                    temp = [atom_in_head, atom_in_body]
                    self._rule.append(temp)

                else:

                    atom_in_body = set()
                    atom_in_head = set()
                    if len(o.head) == 1:
                        atom_in_head.update(o.head)
                    else:
                        atom_in_body.update(o.body)
                    self._unary.update(o.atoms)
                    temp = [atom_in_head, atom_in_body]
                    self._rule.append(temp)
                for a in o.atoms.difference(self._atomToVertex):
                    # add mapping for atom not yet mapped
                    self._atomToVertex[a] = i
                    self._max = i
                    i += 1

    def _generateCompletionRule(self):
        self._completion_rule = []
        head = set()
        for rule in self._rule:
            # print(rule)
            # split head rule in multiple rules
            if len(rule[0]) > 0:  # Rule
                for head_in_rule in rule[0]:
                    head.add(head_in_rule)
            else:  # Integrity constraints
                complete_rule = [[], [rule[1]]]
                self._completion_rule.append(complete_rule)
        for h in head:
            body = []
            for rule in self._rule:
                if h in rule[0] and rule[1] not in body:
                    if rule[1]:
                        body.append(rule[1])
            complete_rule = [[h], body]

            self._completion_rule.append(complete_rule)

    def _get_loop(self):
        # here we will compute set of atoms which has loops , so we can compute external support afterwards.
        atoms_in_head = set()
        atoms_in_body = set()
        for rule in self._rule:
            iterator = filter(get_positive_value, rule[1])
            positive_atoms = set(iterator)  # positive atoms in body
            if len(positive_atoms) > 0:
                atoms_in_body.update(positive_atoms)
                atoms_in_head.update(rule[0])
                # should only consider atoms in head which has at least one positive atom in body.
        loop_atoms = atoms_in_head.intersection(atoms_in_body)
        # atoms_loop should contain the only atoms that can have loops.
        # loop sets can be only part of atoms_loop.
        self._loop_rule = get_rule_loop(self._rule, loop_atoms)
        g = Graph(len(loop_atoms))
        for rule in self._loop_rule:
            for head in rule[0]:
                for body in rule[1]:
                    # loop rule might contains atoms that will not be part of loop
                    if head in list(loop_atoms) and body in list(loop_atoms):
                        g.addEdge(body, head)

        self._loop = g.cycles()

    def _setPrimalGraph(self):
        # vertices
        for u in self._unary:
            self._graph.add_node(u)
        # completion Rules
        for complete_rule in self._completion_rule:
            atoms = set()
            for head in complete_rule[0]:
                if head != 0:
                    atoms.add(head)  # head
            for body in complete_rule[1]:
                atoms.update(tuple(map(abs, body)))  # body
            self._graph.add_hyperedge(tuple(map(lambda x: self._atomToVertex[x], atoms)))
        # External Support
        for ES in self._externalSupport:
            atoms = set()
            for rules in ES:
                atoms.update(rules[0])
                atoms.update(tuple(map(abs, rules[1])))
            self._graph.add_hyperedge(tuple(map(lambda x: self._atomToVertex[x], atoms)))

    def _generatePrimalGraph(self):

        self._generateRule()
        self._generateCompletionRule()
        self._generateExternalSupports()
        self._graph = hypergraph.Hypergraph()
        self._setPrimalGraph()
        # print(self._graph)

    def solve_problem(self, file, cfg):
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
            sys.exit(0)

        admin_db = DBAdmin.from_cfg(cfg["db_admin"])
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        signal.signal(signal.SIGUSR1, signal_handler)
        pool = BlockingThreadedConnectionPool(1, cfg["db"]["max_connections"], **cfg["db"]["dsn"])
        problem = SharpSat(file, pool, **cfg["dpdb"])

        # print(self._completion_rule)

        problem.prepare_input(rule=self._completion_rule, atoms_vertex=self._atomToVertex,
                              external_support=self._externalSupport)
        problem.set_td(self._td)
        problem.setup()
        problem.solve()

    def _decomposeGraph(self, cfg):
        # Run htd
        p = subprocess.Popen(
            [os.path.join(os.getcwd()+ cfg["htd"]["path"], "bin/htd_main"), "--seed", "12342134",
             "--input", "hgr"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

        logger.info("Running htd")

        p.stdin.write(self._graph.repr().encode())
        p.stdin.flush()

        p.stdin.close()
        tdr = TdReader.from_stream(p.stdout)
        p.wait()
        logger.info("TD computed")

        logger.info("Parsing tree decomposition")

        self._td = TreeDecomp(tdr.num_bags, tdr.tree_width, tdr.num_orig_vertices, tdr.root, tdr.bags,
                              tdr.adjacency_list)

        logger.info(
            f"Tree decomposition #bags: {self._td.num_bags} tree_width: {self._td.tree_width} #vertices: {self._td.num_orig_vertices} #leafs: {len(self._td.leafs)} #edges: {len(self._td.edges)}")
        # logger.info(self._td.nodes)

    def _generateClausesCompleteRule(self):
        print("p cnf " + str(len(self._atomToVertex)) + " " + str(len(self._completion_rule)))
        for complete_rule in self._completion_rule:
            clause = ""
            ## Head
            if complete_rule[0] > 0:
                clause += str(self._atomToVertex[complete_rule[0]]) + " "
            if complete_rule[0] < 0:
                clause += str(self._atomToVertex[complete_rule[0] * -1] * -1) + " "
            ## Body
            for body in complete_rule[1]:
                for b in body:
                    if b < 0:
                        clause += str(self._atomToVertex[b * -1]) + " "
                    else:
                        clause += str(self._atomToVertex[b] * -1) + " "
            clause += "0"
            print(clause)

    def _generateClausesRule(self):
        print("p cnf " + str(len(self._atomToVertex)) + " " + str(len(self._rule)))
        for r in self._rule:
            clause = ""
            for head in r[0]:
                if head > 0:
                    clause += str(self._atomToVertex[head]) + " "
                else:
                    clause += str(self._atomToVertex[head * -1] * -1) + " "
            for body in r[1]:
                if body < 0:
                    clause += str(self._atomToVertex[body * -1]) + " "
                else:
                    clause += str(self._atomToVertex[body] * -1) + " "
            clause += "0"
            print(clause)

    def _generateExternalSupports(self):
        self._get_loop()  # loop(P)
        self._externalSupport = [get_rule_No_loop(self._rule, loop_atoms) for loop_atoms in self._loop]
        logger.info(" Generating External Support")
        logger.info(self._loop)
        logger.info(self._externalSupport)

    def main(self, clingo_control, files):
        """
        Entry point of the application registering the propagator and
        implementing the standard ground and solve functionality.
        """
        subprocess.call(os.getcwd() + "/dpdb/purgeDB.sh")
        if not files:
            files = ["-"]

        self.control = clingoext.Control()
        cfg = read_cfg("./config.json")
        for path in files:
            self.control.add("base", [], self._read(path))

        self.control.ground()

        logger.info("------------------------------------------------------------")
        logger.info("   Grounded Program")
        logger.info("------------------------------------------------------------")
        # logger.info(self.control.ground_program)
        logger.info("------------------------------------------------------------")
        logger.info(" Generating Primal Graph")
        self._generatePrimalGraph()
        #  logger.info("------------------------------------------------------------")
        # logger.info(" Generating Clauses")
        # self._generateClauses_rule()
        logger.info("------------------------------------------------------------")
        logger.info(" Decomposing Graph")
        self._decomposeGraph(cfg)

        setup_debug_sql()

        self.solve_problem(files, cfg)


if __name__ == "__main__":
    sys.exit(int(clingoext.clingo_main(Application(), sys.argv[1:])))
