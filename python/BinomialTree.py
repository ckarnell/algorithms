class Node():
    def __init__(self, data=None):
        self.data = data
        self.child_nodes = []

class BinomialTree():
    def __init__(self, order = 0):
        self.root = Node()
        self.order = order
        self.children = []
        self.build(self.root, self.order)

    def build(self, root, order):
        for x in range(order):
            if x:
                new_node = Node()
                root.child_nodes.append(new_node)
                self.build(new_node, order-1)

    def print_tree(self):
        def print_recurse(root):
            print root
            for node in root.child_nodes:
                print_recurse(node)
        print_recurse(self.root)

if __name__ == "__main__":
    pass
