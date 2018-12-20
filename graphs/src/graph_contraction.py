from numpy.random import choice

def graph_cut(edges):
    return len(list(edges.values())[0])

def graph_contraction(vertices, edges, weights):
    """Run Karger's contraction algorithm on weighted graph."""
    while len(vertices) > 2:
        # choose random edge from graph
        v = choice(sorted(vertices.keys()), p=[f / sum(weights) for f in sorted(weights.keys())])
        u = choice(list(edges[v]))
        # print(f"choosen edge: {v}-{u}")
        # append all edges to vertex v but remove self-loops (e != v and e != u)
        edges[v].update(edges[u])
        edges[v] -= {u, v}
        # update vertices adjacent to v
        vertices[v] += vertices[u]
        weights[v] = len(edges[v])
        for e in edges[u]:

            # re-linking edges from anihilated vertex u to anihilating vertex v
            if e != v and u in edges.get(e, []):
                # vertex u doesn't exists any more independently
                edges[e] -= {u}
                edges[e].update({v})
                # edges[e] = set([c if c != u else v for c in edges[e]])
        del edges[u]
        del vertices[u]
        del weights[u]
    return vertices, edges, weights


class Graph():
    """Graph class."""

    def __init__(self, connections_string):
        """Initialize Graph from dictionary of connections"""
        self.vertices = dict()
        self.edges = dict()
        # weights correspond to number of vertices adjacent to ith vertex. Use later for sampling edges
        self.weights = dict()
        self._cut = None
        for line in connections_string.splitlines():
            vertex_source, *vertices = list(map(int,line.split("\t")))
            # vertex with name v will initially containt only himself
            self.vertices[vertex_source] = [vertex_source]
            self.edges[vertex_source] = set(vertices)
            self.weights[vertex_source] = len(self.edges[vertex_source])

    def contract(self):
        self.vertices, self.edges, self.weights = graph_contraction(self.vertices, self.edges, self.weights)

    @property
    def cut(self):
        """Calculate cut in contracted graph"""
        if len(self.vertices) > 2:
            raise ValueError("Graph not contracted, no cut to calculate.")
        if self._cut is None:
            self._cut = graph_cut(self.edges)
        return self._cut