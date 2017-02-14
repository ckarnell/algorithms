class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree():
    def __init__(self, init_value=None):
        if isinstance(init_value, int) or isinstance(init_value, float):
            self.root_node = Node(init_value)
            self.size = 1
        else:
            self.root_node = None
            self.size = 0

    # Add a node to the tree, or make the root node the argument
    # node if the tree is empty.
    def add_node(self, value):
        current_node = self.root_node

        if not current_node:
            self.root_node = Node(value)
            self.size += 1
        else:
            self.size += self.insert(value, current_node)

    # Helper for add_node. Adds the node to the tree if it's value is new
    # and returns the increase in size of the total tree.
    def insert(self, value, current_node):
        if value < current_node.value:
            if  not current_node.left:
                current_node.left = Node(value)
                return 1
            else:
                return self.insert(value, current_node.left)
        elif value > current_node.value:
            if  not current_node.right:
                current_node.right = Node(value)
                return 1
            else:
                return self.insert(value, current_node.right)
        else:
            # If the value is already in the list, return.
            return 0

    # Returns an inorder list of the nodes.
    def inorder_traversal(self):
        def inorder_recurse(current_node, ordered_list):
            # Reached an empty node.
            if not current_node:
                return []

            # Go left.
            ordered_list.extend(inorder_recurse(current_node.left, []))
            # Add the current node.
            ordered_list.append(current_node.value)
            # Go right.
            ordered_list.extend(inorder_recurse(current_node.right, []))

            return ordered_list

        return inorder_recurse(self.root_node, [])

    # Returns a preorder list of the nodes.
    def preorder_traversal(self):
        def preorder_recurse(current_node, ordered_list):
            # Reached an empty node.
            if not current_node:
                return []

            # Add the current node.
            ordered_list.append(current_node.value)
            # Go left.
            ordered_list.extend(preorder_recurse(current_node.left, []))
            # Go right.
            ordered_list.extend(preorder_recurse(current_node.right, []))

            return ordered_list

        return preorder_recurse(self.root_node, [])

    # Returns a postorder list of the nodes.
    def postorder_traversal(self):
        def postorder_recurse(current_node, ordered_list):
            # Reached an empty node.
            if not current_node:
                return []

            # Go left.
            ordered_list.extend(postorder_recurse(current_node.left, []))
            # Go right.
            ordered_list.extend(postorder_recurse(current_node.right, []))
            # Add the current node.
            ordered_list.append(current_node.value)

            return ordered_list

        return postorder_recurse(self.root_node, [])

if __name__ == "__main__":
    import unittest

    class BinarySearchTreeTest(unittest.TestCase):
        def setUp(self):
            self.btree = BinarySearchTree()

        def test_initialize_empty_btree(self):
            self.assertEqual(self.btree.root_node, None)
            self.assertEqual(self.btree.size, 0)

        def test_initialize_btree_with_node(self):
            btree = BinarySearchTree(5.5)
            self.assertEqual(btree.root_node.value, 5.5)
            self.assertEqual(btree.root_node.left, None)
            self.assertEqual(btree.root_node.right, None)
            self.assertEqual(btree.size, 1)

        def test_add_node_to_empty_btree(self):
            self.btree.add_node(6)
            self.assertEqual(self.btree.root_node.value, 6)
            self.assertEqual(self.btree.root_node.left, None)
            self.assertEqual(self.btree.root_node.right, None)
            self.assertEqual(self.btree.size, 1)

        def test_add_lesser_node_to_tree_of_length_one(self):
            self.btree.add_node(6)
            self.btree.add_node(3)
            self.assertEqual(self.btree.root_node.value, 6)
            self.assertEqual(self.btree.root_node.left.value, 3)
            self.assertEqual(self.btree.root_node.right, None)
            self.assertEqual(self.btree.size, 2)

        def test_add_greater_node_to_tree_of_length_one(self):
            self.btree.add_node(6)
            self.btree.add_node(10)
            self.assertEqual(self.btree.root_node.value, 6)
            self.assertEqual(self.btree.root_node.left, None)
            self.assertEqual(self.btree.root_node.right.value, 10)
            self.assertEqual(self.btree.size, 2)

        def test_add_two_nodes_to_tree_of_length_one(self):
            self.btree.add_node(6)
            self.btree.add_node(3)
            self.btree.add_node(4)
            self.assertEqual(self.btree.root_node.value, 6)
            self.assertEqual(self.btree.root_node.left.value, 3)
            self.assertEqual(self.btree.root_node.left.right.value, 4)

        def test_inorder_traversal_on_large_tree(self):
            ordered_list = [8, 3, 1, 6, 4, 7, 10, 14, 13]
            for val in ordered_list:
                self.btree.add_node(val) 
            inorder_list = self.btree.inorder_traversal()
            desired_result = [1, 3, 4, 6, 7, 8, 10, 13, 14]
            self.assertEqual(inorder_list, desired_result)

        def test_preorder_traversal_on_large_tree(self):
            ordered_list = [8, 3, 1, 6, 4, 7, 10, 14, 13]
            for val in ordered_list:
                self.btree.add_node(val) 
            preorder_list = self.btree.preorder_traversal()
            desired_result = [8, 3, 1, 6, 4, 7, 10, 14, 13]
            self.assertEqual(preorder_list, desired_result)

        def test_postorder_traversal_on_large_tree(self):
            ordered_list = [8, 3, 1, 6, 4, 7, 10, 14, 13]
            for val in ordered_list:
                self.btree.add_node(val) 
            postorder_list = self.btree.postorder_traversal()
            desired_result = [1, 4, 7, 6, 3, 13, 14, 10, 8]
            self.assertEqual(postorder_list, desired_result)

    unittest.main()
