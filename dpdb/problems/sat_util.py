# -*- coding: future_fstrings -*-
from dpdb.problem import *
from collections import defaultdict


class hashabledict(dict):
    def __hash__(self):
        return hash(frozenset(self))


def cnf2primal(num_vars, clauses, var_clause_dict=defaultdict(set)):
    edges = set([])
    for clause in clauses:
        atoms = [abs(lit) for lit in clause]
        clause_set = hashabledict({frozenset(atoms): frozenset(clause)})
        for i in atoms:
            var_clause_dict[i].add(clause_set)
            for j in atoms:
                if i < j:
                    edges.add((i, j))
    return (num_vars, edges)


def td_node_column_def(var):
    return (var2col(var), "BOOLEAN")


def lit2var(lit):
    return var2col(abs(lit))


def lit2val(lit):
    return str(lit > 0)


def lit2expr(lit):
    if lit > 0:
        return var2col(lit)
    else:
        return "NOT {}".format(lit2var(lit))


def lit2expr_body(lit):
    if lit < 0:
        return lit2var(lit)
    else:
        return "NOT {}".format(lit2var(lit))


# Filter for Models
def filter(node, rules, atoms_vertex):
    vertice_set = set(node.vertices)

    cur_cl = []
    selected_rules = []
    # to get rules that need to be applied on selected table
    for r in rules:
        vertices = set()
        head_rule = []
        body_rule = []
        for head in r[0]:
            vertices.add(atoms_vertex[abs(head)])
            head_rule.append(atoms_vertex[abs(head)])
        for body in r[1]:
            part_body_rule = []
            for part_body in body:
                vertices.add(atoms_vertex[abs(part_body)])
                if part_body <0:
                    part_body_rule.append(atoms_vertex[abs(part_body)]*-1)
                else:
                    part_body_rule.append(atoms_vertex[abs(part_body)])
            body_rule.append(part_body_rule)
        if vertices <= vertice_set:
            cur_cl.append(vertices)
            selected_rule = [head_rule, body_rule]
            selected_rules.append(selected_rule)
    #print(selected_rules)
    if len(cur_cl) > 0:

        return  "WHERE {0}".format(
            "((({0})))".format(")) AND ((".join(
                ["".join(
                    # one direction <-
                    ["".join(" OR ".join(map(lit2expr, rule[0]))),  # head
                     ") OR(",
                     " AND ".join([")OR(".join(map(lit2expr_body, body_part)) for body_part in rule[1]])
                     # other direction ->

                        ,"))AND (("
                        , "".join(" AND ".join(map(lit2expr_body, rule[0]))),  # head
                     ")OR (",
                     " OR ".join([")AND(".join(map(lit2expr, body_part)) for body_part in rule[1]])
                     ]  if rule[0]  # body

                    # Constraints only
                    # one direction <-
                    else ["".join([" OR ".join(map(lit2expr_body, body_part)) for body_part in rule[1]])
                          # other direction ->
                          ]




                ) for rule in selected_rules]
            )
            ))
        # print(selected_rules)



def store_clause_table(db, clauses):
    db.drop_table("sat_clause")
    num_vars = len(clauses)
    db.create_table("sat_clause", map(td_node_column_def, range(1, num_vars + 1)))
    for clause in clauses:
        db.insert("sat_clause", list(map(lit2var, clause)), list(map(lit2val, clause)))