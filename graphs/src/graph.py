from edge import Edge
from graph_contraction import graph_contraction, graph_cut
from collections import defaultdict

class Graph:
    """Not directed graph implementation."""
    def __init__(self, connections_string):
        """Initialize Graph from dictionary of connections

        Attrs:
            vertices - vertices that are inside each original vertex
            edges - set of edges for graph
            cut - cut value
        """

        self.vertices = defaultdict(set)
        self.adjacent = defaultdict(set)
        self.edges = set()
        # weights correspond to number of vertices adjacent to ith vertex. Use later for sampling edges
        self._cut = None
        for line in connections_string.splitlines():
            vertex_source, *vertices = list(map(int, line.split("\t")))
            # vertex with name v will initially containt only himself
            self.vertices[vertex_source].update(set([vertex_source]))
            self.adjacent[vertex_source].update(set(vertices))
            self.edges.update({Edge(vertex_source, vertex_to) for vertex_to in vertices})

    def contract(self):
        self.vertices, self.adjacent, self.edges = graph_contraction(self.vertices, self.adjacent, self.edges)

    @property
    def cut(self):
        """Calculate cut in contracted graph"""
        if len(self.vertices) > 2:
            raise ValueError("Graph not contracted, no cut to calculate.")
        if self._cut is None:
            self._cut = graph_cut(self.adjacent)
        return self._cut
