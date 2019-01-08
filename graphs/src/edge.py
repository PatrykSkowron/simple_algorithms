class Edge:
    """Implementation of undirected edge.
    Hash and comparision functions help with maintaining sets and dicts of edges without duplicates.
    """
    def __init__(self, vertex_source, vertex_to):
        """There is no difference in order of vertices connected, what ensures undirected edge."""
        self.edge = tuple(sorted([vertex_source, vertex_to]))

    def __hash__(self):
        return hash(self.edge)

    def __eq__(self, other):
        return self.edge == other.edge

    def __str__(self):
        return self.edge