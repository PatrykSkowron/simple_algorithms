class Edge:
    def __init__(self, vertex_source, vertex_to):
        self.edge = tuple(sorted([vertex_source, vertex_to]))

    def __hash__(self):
        return hash(self.edge)

    def __eq__(self, other):
        return self.edge == other.edge

    def __str__(self):
        return self.edge