from numpy.random import choice
from copy import deepcopy
from edge import Edge


def graph_cut(adjacent):
    return len(list(adjacent.values())[0])

def graph_contraction(vertices, adjacent, edges):
    vertices = deepcopy(vertices)
    edges = deepcopy(edges)
    """Run Karger's contraction algorithm on weighted graph."""
    while len(vertices) > 2:
        # choose random edge from graph
        chosen_edge = choice(list(edges))
        v, u = chosen_edge.edge
        # print(f"choosen edge: {v}-{u}")
        # append all edges to vertex v but remove self-loops (e != v and e != u)
        # update vertices adjacent to v
        vertices_joined = vertices[u]
        adjacent_joined = adjacent[u]
        adjacent[v].update(adjacent_joined)
        # avoid self-loops
        adjacent[v] -= {v}
        vertices[v].update(vertices_joined)

        edges_anihilated = {Edge(u, v_target) for v_target in adjacent_joined}
        edges_created = {Edge(v, v_target) for v_target in adjacent_joined}
        #avoid self-loops
        edges_created -= {Edge(v, v)}
        edges -= edges_anihilated
        edges.update(edges_created)
        # for e in edges:
        #     # re-linking edges from anihilated vertex u to anihilating vertex v
        #     if e != v and u in edges.get(e, []):
        #         # vertex u doesn't exists any more independently
        #         edges[e] -= {u}
        #         edges[e].update({v})
        # del edges[u]
        del vertices[u]
        del adjacent[u]
    return vertices, adjacent, edges

