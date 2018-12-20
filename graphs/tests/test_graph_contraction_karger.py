import unittest
from time import time
from graph_contraction import Graph, graph_contraction, graph_cut

NUMBER_SAMPLE_CUT = 10

def log_time(function, *args, **kwargs):
    start = time()
    ret = function(*args, **kwargs)
    end = time()
    return ([end - start, ret])

class Test_Graph(unittest.TestCase):

    def _testing(self, str):
        print("INIT GRAPH...")
        graph = Graph(str)
        print("CONTRACTING GRAPH...")
        graph.contract()
        print("GRAPH CONTRACTED")
        print("GRAPH CUT: {graph.cut}")

    def _testing_min_cut(self, str):
        graph = Graph(str)
        cuts = []
        print("RUNNING CONTRACTION ALGORITHM {n} TIMES")
        for i in range(NUMBER_SAMPLE_CUT):
            v,e,w = graph_contraction(graph.vertices.copy(), graph.edges.copy(), graph.weights.copy())
            cut = graph_cut(e)
            print(f"{i} GRAPH CUT: {cut}")
            cuts.append(cut)
        print(cuts)

    def test_simple(self):
        str = """1	2	4
                2	1	3	4
                3	2	4
                4	1	2	3"""
        self._testing(str)
        self._testing_min_cut(str)

    def test_big_graph(self):
        file = 'resources/graph_big'
        with open(file, 'r') as file_input:
            input_string = file_input.read()

        self._testing(input_string)
        self._testing_min_cut(input_string)

    def test_empty(self):
        str =""
        self._testing(str)

    def test_two_vertices(self):
        str = """1	2
        2	1"""
        self._testing(str)
        self._testing_min_cut(str)

    # def test_two_components(self):
    #     str="""1	2
    #     2	1
    #     3	4
    #     4	3"""
    #     self._testing(str)
    #     self._testing_min_cut(str)


if __name__ == '__main__':
    unittest.main()