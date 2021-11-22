import unittest
from bellman_ford import Graph


class BellmanFordTest(unittest.TestCase):
    def setUp(self):
        self.new_graph = Graph(4)
        self.new_graph.add_vertex(0, 1, 2)
        self.new_graph.add_vertex(1, 2, -3)
        self.new_graph.add_vertex(1, 3, -2)
        self.new_graph.add_vertex(2, 3, -3)

    def test_bellman_ford_(self):
        self.assertEqual(self.new_graph.bellman_ford(0), [0, 2, -1, -4])

    def test_bellman_ford_with_ing(self):
        self.assertEqual(self.new_graph.bellman_ford(1), [float("Inf"), 0, -3, -6])

unittest.main()