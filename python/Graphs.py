class Graph():
    def __init__(self):
        self.nodes = []
        self.edges = {}

    # Add a node name (string) to the graph.
    def add_node(self, node):
        assert isinstance(node, str), "Node names must be strings"
        self.nodes.append(node)
        self.edges[node] = []

    # Add an edge to the graph from one node to another.
    def add_edge(self, from_node, to_node):
        # Both nodes must already be added to the graph.
        assert (from_node in self.nodes), "The from node must already be in the graph"
        assert(to_node in self.nodes), "The from node must already be in the graph"
        self.edges[from_node].append(to_node)

if __name__ == "__main__":
    import unittest

    class GraphTest(unittest.TestCase):
        def setUp(self):
            pass

        def test_add_node_a(self):
            graph = Graph()
            graph.add_node('a')
            self.assertEqual(graph.nodes, ['a'])
            self.assertEqual(graph.edges, {'a':[]})

        def test_add_two_nodes(self):
            graph = Graph()
            graph.add_node('a')
            graph.add_node('b')
            self.assertEqual(graph.nodes, ['a', 'b'])
            self.assertEqual(graph.edges['a'], [])
            self.assertEqual(graph.edges['b'], [])

        def test_add_edge(self):
            graph = Graph()
            graph.add_node('a')
            graph.add_node('b')
            graph.add_edge('a', 'b')
            self.assertEqual(graph.edges['a'], ['b'])

    unittest.main()
