"""
Main module providing the application logic.
"""

import sys
# from textwrap import dedent
from collections import OrderedDict
import clingo
import clingoext
from pprint import pprint



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
        self.version = "0.0.1"
        self.config = AppConfig()

    def _read(self, path):
        if path == "-":
            return sys.stdin.read()
        with open(path) as file_:
            return file_.read()


    def main(self, clingo_control, files):
        """
        Entry point of the application registering the propagator and
        implementing the standard ground and solve functionality.
        """
        if not files:
            files = ["-"]

        control = clingoext.Control()

        for path in files:
            control.add("base", [], self._read(path))

        control.ground()

        print("------------------------------------------------------------")
        print("   Grounded Program")
        print("------------------------------------------------------------")
        pprint(control.ground_program.objects)
        print("------------------------------------------------------------")
        print(control.ground_program)
        print("-------------------------------------------------------------")




if __name__ == "__main__":
    sys.exit(int(clingoext.clingo_main(Application(), sys.argv[1:])))
