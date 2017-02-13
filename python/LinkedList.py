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
        if current_node == None:
            raise IndexError, "Can't remove a node from an empty linked list"
        elif current_node.data == data:
            self.head = current_node.next_node
            self.length -= 1
        else:
            while current_node.next_node and current_node.data != data:
                previous_node = current_node
                current_node = current_node.next_node
            if current_node.next_node:
                previous_node.next_node = current_node.next_node
                self.length -= 1
            else:
                raise IndexError, "There is no node with the input data"

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

        def test_prepend_node_on_empty_linked_list(self):
            node = Node("test")
            self.ll.prepend_node(node)
            self.assertEqual(self.ll.head, node)
            self.assertEqual(self.ll.length, 1)

        def test_prepend_multiple_nodes(self):
            node1 = Node(10)
            node2 = Node("test")
            self.ll.prepend_node(node1)
            self.ll.prepend_node(node2)
            self.assertEqual(self.ll.head, node2)
            self.assertEqual(self.ll.head.next_node, node1)
            self.assertEqual(self.ll.length, 2)

        def test_remove_node_from_empty_list(self):
            try:
                self.ll.remove_node(5)
            except IndexError:
                self.assertEqual(self.ll.head, None)
                self.assertEqual(self.ll.length, 0)

        def test_remove_existing_node_from_list_of_length_one(self):
            node = Node("test")
            self.ll.append_node(node)
            self.ll.remove_node(node.data)
            self.assertEqual(self.ll.head, None)
            self.assertEqual(self.ll.length, 0)

        def test_remove_existing_nodes_from_list_of_length_four(self):
            nodes = [Node(5), Node("test"), Node(True), Node(1.5)]
            for node in nodes:
                self.ll.append_node(node)

            # Remove two inner nodes.
            self.ll.remove_node("test")
            self.ll.remove_node(True)
            self.assertEqual(self.ll.head.data, 5)
            self.assertEqual(self.ll.head.next_node.data, 1.5)
            self.assertEqual(self.ll.head.next_node.next_node, None)
            self.assertEqual(self.ll.length, 2)
            # Remove the head.
            self.ll.remove_node(5)
            self.assertEqual(self.ll.head.data, 1.5)
            self.assertEqual(self.ll.head.next_node, None)
            # Remove the last node.
            self.ll.remove_node(1.5)
            self.assertEqual(self.ll.head, None)
            self.assertEqual(self.ll.length, 0)

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
