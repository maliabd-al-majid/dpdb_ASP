from collections import defaultdict
import logging

from dpdb.problem import var2tab_alias

logger = logging.getLogger(__name__)
def get_positive_value(atom):
    return atom > 0


def get_rule_loop(rules, atoms):
    loop_rules = list()
    for rule in rules:

        if len(atoms.intersection(rule[0])) > 0 and len(atoms.intersection(rule[1])) > 0:
            # we use the observation that rule must contain two occurrences of atoms or more in rule to be part of loop.
            loop_rules.append(rule)
    return loop_rules


def get_rule_No_loop(rules, atoms):
    NoLoop_rules = list()
    atoms_ES = set()
    for rule in rules:

        if len(atoms.intersection(rule[0])) > 0 and len(atoms.intersection(rule[1])) == 0:
            atoms_ES.update(rule[0])
            # we use the observation that rule must contain two occurrences of atoms or more in rule to be part of loop.
            NoLoop_rules.append(rule)
    # create new rule with empty body for atoms without External support
    for atom in atoms.difference(atoms_ES):
        NoLoop_rules.append([set([atom]), set()])
    return NoLoop_rules


def read_cfg(cfg_file):
    import json

    with open(cfg_file) as c:
        cfg = json.load(c)
    return cfg


def flatten_cfg(dd, filter=[], separator='.', prefix=''):
    if prefix.startswith(tuple(filter)):
        return {}

    if isinstance(dd, dict):
        return {prefix + separator + k if prefix else k: v
                for kk, vv in dd.items()
                for k, v in flatten_cfg(vv, filter, separator, kk).items()
                if not (prefix + separator + k).startswith(tuple(filter))
                }
    elif isinstance(dd, list):
        return {prefix: " ".join(dd)}
    else:
        return {prefix: dd}


def lit2rule(lit):
    if lit > 0:
        return "x_{}".format(abs(lit))
    else:
        return "not x_{}".format(abs(lit))



def var2col2(node, var, minors):
    # if node.is_minor(var):
    if var in minors:
        return "{}.val".format(var2tab_alias(node, var))
    else:
        return f"v{var}"


def lit2var2(node, lit, minors):
    return var2col2(node, abs(lit), minors)


def lit2expr2(node, lit, minors):
    if lit > 0:
        return lit2var2(node, lit, minors)
    else:
        return "NOT {}".format(lit2var2(node, lit, minors))





def lit2expr2body(node, lit, minors):
    if lit < 0:
        return lit2var2(node, lit, minors)
    else:
        return "NOT {}".format(lit2var2(node, lit, minors))


def rule2expr(head, body, node, minor_vertices):  # direction -->
    f = " ( "
    if head:
        f += "".join(" AND ".join([lit2expr2body(node, c, minor_vertices) for c in head]))
    else:
        f += "True"
    f += ") OR ("
    f += "".join(" AND ".join([lit2expr2(node, c, minor_vertices) for c in body]))
    f += " ) "
    return f


def rule2expr2(head, body, node, minor_vertices):  # direction <--
    f = " ( "
    if head:
        f += "".join(" OR ".join([lit2expr2(node, c, minor_vertices) for c in head]))
    else:
        f += "False"
    f += ") OR ("
    f += "".join(" OR ".join([lit2expr2body(node, c, minor_vertices) for c in body]))
    f += " ) "
    return f

class hashabledict(dict):
    def __hash__(self):
        return hash(frozenset(self))


def _add_directed_edge(edges, adjacency_list, vertex1, vertex2):
    if vertex1 == vertex2:
        return

    if vertex1 in adjacency_list:
        adjacency_list[vertex1].add(vertex2)
    else:
        adjacency_list[vertex1] = {vertex2}
    if vertex1 < vertex2:
        edges.add((vertex1, vertex2))

def covered_rules(rules, vertices):
    vertice_set = set(vertices)
    cur_cl = set()
    #print(rules)
   # print(vertice_set)
    for v in vertices:
        candidates = rules[v]
       # print(rules[v])
        for d in candidates:
            for key, val in d.items():
                if key.issubset(vertice_set):
                    cur_cl.add(val)
   # print(cur_cl)
   # print(vertice_set)
    return list(map(list,cur_cl))

def program2primal(num_atoms, rules, atom_rule_dict=defaultdict(set), ret_adj=False):
    edges = set([])
    adj = {}
    #print(rules)
    for rule in rules:
        atoms = [abs(lit) for lit in frozenset().union(*rule)]
    #    print(atoms)
        rule_set = hashabledict({frozenset(atoms): frozenset(rule)})  # might need to convert rule into one set
      #  print(rule_set)
      #  print(rule_set)
        for i in atoms:
            atom_rule_dict[i].add(rule_set)

            for j in atoms:
                _add_directed_edge(edges, adj, i, j)
                _add_directed_edge(edges, adj, j, i)
       # print(atom_rule_dict)
    if ret_adj:
        logger.info("atoms:"+str(num_atoms))
        logger.info("edges"+str(edges))
        logger.info("adj"+str(adj))
        #print("------------------------------------------------------")
        return num_atoms, edges, adj
    else:

        return num_atoms, edges
