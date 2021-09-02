from collections import defaultdict

# used for Cyclic Graphs to generate all cycles in graph
class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def _dfs(self, start, end):
        fringe = [(start, [])]
        while fringe:
            state, path = fringe.pop()
            if path and state == end:
                yield path
                continue
            for next_state in self.graph[state]:
                if next_state in path:
                    continue
                fringe.append((next_state, path + [next_state]))

    def cycles(self):
        try:
            cycles = [[node] + path for node in self.graph for path in self._dfs(node, node)]
            return set(frozenset(s) for s in cycles)
        except:
            return set(frozenset([]))
