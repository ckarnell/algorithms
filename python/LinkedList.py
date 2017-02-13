class Node():
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.length = 0

    # Adds a node to the tail of the linked list.
    def append_node(self, node):
        tail = self.head
        if tail != None:
            # Find the first node that doesn't point to another node.
            while tail.next_node:
                tail = tail.next_node
            tail.next_node = node
        else:
            self.head = node

        self.length += 1

    # Makes the argument node the linked list's new head node.
    def prepend_node(self, node):
        previous_head = self.head
        self.head = node
        self.head.next_node = previous_head
        self.length += 1

    # Removes the first node with the given data.
    # Returns an error if there isn't such a node.
    def remove_node(self, data):
        current_node = self.head
        if current_node.data == data:
            self.head = current_node.next_node
        else:
            while current_node.next_node and current_node.data != data:
                previous_node = current_node
                current_node = current_node.next
            if current_node.next_node:
                previous_node.next_node = current_node.next_node
                self.length -= 1
            else:
                print "There is no node with the input data"
                raise IndexError

    # Prints the nodes. The "out" argument is used only for testing.
    def print_nodes(self, out=None):
        current_node = self.head
        for ind in range(self.length):
            if out:
                out.write("Node {}: {}".format(ind+1, current_node.data))
            else:
                print "Node {}: {}".format(ind+1, current_node.data)
            current_node = current_node.next_node

if __name__ == '__main__':
    import unittest

    class LinkedListTest(unittest.TestCase):
        def setUp(self):
            self.ll = LinkedList()

        def test_instantiate_linked_list(self):
            self.assertEqual(self.ll.length, 0)
            self.assertEqual(self.ll.head, None)

        def test_instantiate_node_data_types(self):
            node_int = Node(8)
            node_float = Node(5.0)
            node_string = Node("test")
            node_bool = Node(True)
            self.assertEqual(node_int.data, 8)
            self.assertEqual(node_int.next_node, None)
            self.assertEqual(node_float.data, 5.0)
            self.assertEqual(node_float.next_node, None)
            self.assertEqual(node_string.data, "test")
            self.assertEqual(node_string.next_node, None)
            self.assertEqual(node_bool.data, True)
            self.assertEqual(node_bool.next_node, None)

        def test_append_a_node(self):
            node = Node("test")
            self.ll.append_node(node)
            self.assertEqual(self.ll.head, node)
            self.assertEqual(self.ll.length, 1)

        def test_append_two_nodes(self):
            node1 = Node(10)
            node2 = Node("test")
            self.ll.append_node(node1)
            self.ll.append_node(node2)
            self.assertEqual(self.ll.head.data, 10)
            self.assertEqual(self.ll.head.next_node.data, "test")
            self.assertEqual(self.ll.head.next_node.next_node, None)
            self.assertEqual(self.ll.length, 2)

        def test_prepend_node(self):
            node = Node("test")

        def test_print_nodes(self):
            node1, node2, node3 = [Node(5), Node("test"), Node(True)]
            for node in [node1, node2, node3]:
                self.ll.append_node(node)

            from StringIO import StringIO
            out = StringIO()
            self.ll.print_nodes(out=out)
            output = out.getvalue().strip()
            self.assertEqual(output, "Node 1: 5Node 2: testNode 3: True")

    unittest.main()
