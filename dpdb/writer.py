from asp.asp_util import lit2rule
from dpdb.problems.sat_util import lit2expr


class Writer(object):
    def write(self, str):
        pass

    def writeline(self, str):
        self.write(str)
        self.write("\n")

    def flush(self):
        pass

    def write_gr(self, num_vertices, edges):
        self.writeline("p tw {0} {1}".format(num_vertices, len(edges)))
        for e in edges:
            self.writeline("{0} {1}".format(e[0], e[1]))
        self.flush()

    def write_graph(self, graph, dimacs):
        gr_string = 'edge' if dimacs else 'htw'
        s = 'p ' if dimacs else ''

        self.write('p %s %s %s\n' % (gr_string, graph.number_of_nodes(), graph.number_of_edges()))
        print(('p %s %s %s\n' % (gr_string, graph.number_of_nodes(), graph.number_of_edges())))
        s = 'e ' if dimacs else ''
        for e_id, nodes in zip(range(graph.number_of_edges()), graph.edges_iter()):
            nodes = ' '.join(map(str, nodes))
            self.write('%s%s %s\n' % (s, e_id + 1, nodes))
            print('%s%s %s\n' % (s, e_id + 1, nodes))
        self.flush()

    def write_td(self, num_bags, tree_width, num_orig_vertices, root, bags, edges):
        self.writeline("s td {0} {1} {2}".format(num_bags, tree_width + 1, num_orig_vertices))
        self.writeline("c r {0}".format(root))
        for b, v in bags.items():
            self.writeline("b {0} {1}".format(b, " ".join(map(str, v))))
        for e in edges:
            self.writeline("{0} {1}".format(e[0], e[1]))

    def write_program(self, rules, projected_atoms=None):
        rules_head = set()
        rules_body = set()
        # print(rules)

        for rule in rules:
            head, body = rule
            rules_head.update(map(abs, head))
            rules_body.update(map(abs, body))
            self.writeline("{}:- {}.".format(" ; ".join(map(lit2rule, head)), " , ".join(map(lit2rule, body))))
        for atom in projected_atoms:
            self.writeline("#show {}/0.".format(lit2rule(abs(atom))))
        choice = "{"
        choice += ";".join(map(lit2rule, rules_body.difference(rules_head)))
        choice += "}."
        self.writeline(choice)
        self.flush()


class StreamWriter(Writer):
    def __init__(self, stream):
        self.stream = stream

    def write(self, str):
        self.stream.write(str.encode())

    def flush(self):
        self.stream.flush()


class FileWriter(Writer):
    def __init__(self, fname, mode="w"):
        self.file_name = fname
        self.mode = mode
        if self.mode[-1] != "b":
            self.mode += "b"

    def __enter__(self):
        self.fd = open(self.file_name, self.mode)
        self.stream_writer = StreamWriter(self.fd)
        return self.stream_writer

    def __exit__(self, type, value, traceback):
        self.fd.close()

    def write(self, str):
        self.fd.write(str)

    def flush(self):
        self.stream_writer.flush()
