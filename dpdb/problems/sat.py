# -*- coding: future_fstrings -*-
import logging
from collections import defaultdict

from dpdb.problem import *

from .sat_util import *

logger = logging.getLogger(__name__)


class Sat(Problem):

    def __init__(self, name, pool, store_formula=False, **kwargs):
        super().__init__(name, pool, **kwargs)
        self.store_formula = store_formula

    def td_node_column_def(self, var):
        return td_node_column_def(var)

    def filter(self, node):
        return filter(node, self.rules, self.atoms_vertices, self.external_support)

    def setup_extra(self):
        def create_tables():
            self.db.ignore_next_praefix()
            self.db.create_table("problem_sat", [
                ("id", "INTEGER NOT NULL PRIMARY KEY REFERENCES PROBLEM(id)"),
                ("num_vars", "INTEGER NOT NULL"),
                ("num_rules", "INTEGER NOT NULL"),
                ("is_sat", "BOOLEAN")
            ])

        def insert_data():
            self.db.ignore_next_praefix()
            self.db.insert("problem_sat", ("id", "num_vars", "num_rules"),
                           (self.id, self.num_vars, self.num_rules))
            if "faster" not in self.kwargs or not self.kwargs["faster"]:
                self.db.ignore_next_praefix()
                self.db.insert("problem_option", ("id", "name", "value"),
                               (self.id, "store_formula", self.store_formula))
                if self.store_formula:
                    store_clause_table(self.db, self.rules)

        create_tables()
        insert_data()

    def prepare_input(self,rule, atoms_vertex, external_support):
        self.atoms_vertices = atoms_vertex
        self.num_vars = len(atoms_vertex)
        self.num_rules = len(rule)
        self.rules = rule
        self.external_support = external_support

    def after_solve(self):
        root_tab = f"td_node_{self.td.root.id}"
        is_sat = self.db.replace_dynamic_tabs(f"(select exists(select 1 from {root_tab}))")
        self.db.ignore_next_praefix()
        sat = self.db.update("problem_sat", ["is_sat"], [is_sat], [f"ID = {self.id}"], "is_sat")[0]
        logger.info("Problem is %s", "SAT" if sat else "UNSAT")


args.specific[Sat] = dict(
    help="Solve SAT instances",
    options={
        "--store-formula": dict(
            dest="store_formula",
            help="Store formula in database",
            action="store_true",
        )
    }
)
