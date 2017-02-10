class DistanceGraph():
    def __init__(self):
        self.nodes = []
        self.edges = {}

    # Add a node name (string) to the graph.
    def add_node(self, node):
        assert isinstance(node, str), "Node names must be strings"
        assert (node not in self.nodes), "Node by that name already in graph"
        self.nodes.append(node)
        self.edges[node] = {}

    # Add an edge to the graph from one node to another.
    def add_edge(self, from_node, to_node, distance):
        # Both nodes must already be added to the graph.
        assert (from_node in self.nodes), "The from node must already be in the graph"
        assert (to_node in self.nodes), "The from node must already be in the graph"
        assert isinstance(int(distance), int), "The distance must be a number"
        assert distance >= 0, "The distance must be greater than 0"
        self.edges[from_node][to_node] = distance
        self.edges[to_node][from_node] = distance

    # Input an origin node and return a dictionary of least distances from the
    # origin node to each node in the graph.
    def dijkstra(self, origin_node):
        assert origin_node in self.nodes, "The origin node must already be in the graph"
        node_distances = {node: -1 for node in self.nodes}
        node_distances[origin_node] = 0
        current_node = origin_node
        unvisited_nodes = self.nodes
        unvisited_nodes.remove(current_node)

        while unvisited_nodes:
            # Compare the edges of current node to existing distance values.
            for node, distance in self.edges[current_node].items():
                if node in unvisited_nodes:
                    if node_distances[node] != -1:
                        total_distance = node_distances[current_node] + distance
                        if total_distance < node_distances[node]:
                            node_distances[node] = total_distance
                    else:
                        node_distances[node] = node_distances[current_node] + distance

            # Find the next shortest path node and make it current.
            next_node = ''
            next_dist = -1
            for node in unvisited_nodes:
                node_dist = node_distances[node]
                if node_dist != -1:
                    if next_dist != -1:
                        if node_distances[node] < next_dist:
                            next_node = node
                            next_dist = node_dist
                    else:
                        next_node = node
                        next_dist = node_dist

            current_node = next_node
            unvisited_nodes.remove(current_node)

        return node_distances

if __name__ == "__main__":
    import unittest

    class GraphTest(unittest.TestCase):
        def setUp(self):
            pass

        def test_add_node_a(self):
            graph = DistanceGraph()
            graph.add_node('a')
            self.assertEqual(graph.nodes, ['a'])
            self.assertEqual(graph.edges, {'a': {}})

        def test_add_two_nodes(self):
            graph = DistanceGraph()
            graph.add_node('a')
            graph.add_node('b')
            self.assertEqual(graph.nodes, ['a', 'b'])
            self.assertEqual(graph.edges['a'], {})
            self.assertEqual(graph.edges['b'], {})

        def test_add_edge(self):
            graph = DistanceGraph()
            graph.add_node('a')
            graph.add_node('b')
            graph.add_edge('a', 'b', 5.6)
            self.assertEqual(graph.edges['a'], {'b': 5.6})

        # Tests the graph on the Dijkstra's algorithm wikipedia page.
        def test_dijkstra(self):
            graph = DistanceGraph()
            for l in list('abcdef'):
                graph.add_node(l)
            graph.add_edge('a', 'b', 7)
            graph.add_edge('a', 'c', 14)
            graph.add_edge('a', 'd', 9)
            graph.add_edge('b', 'e', 15)
            graph.add_edge('c', 'd', 2)
            graph.add_edge('c', 'f', 9)
            graph.add_edge('d', 'e', 11)
            graph.add_edge('e', 'f', 6)

            result = graph.dijkstra('a')
            expected_result = {'a': 0, 'c': 11, 'b': 7, 'e': 20, 'd': 9, 'f': 20}
            self.assertEqual(result, expected_result)

    unittest.main()


