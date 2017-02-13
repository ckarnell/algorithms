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
        # Find the first node that doesn't point to another node.
        while tail.next_node:
            tail = tail.next_node
        tail.next_node = node
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

if __name__ == '__main__':
    import unittest

    class LinkedListTest(unittest.TestCase):
        def setUp(self):
            pass

        def test_instantiate_linked_list(self):
            ll = LinkedList()
            self.assertEqual(ll.length, 0)
            self.assertEqual(ll.head, None)

    unittest.main()
