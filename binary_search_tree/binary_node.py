class BinaryNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert_node(self, value):
        if self.data > value:
            if self.left is not None:
                self.left.insert_node(value)
            else:
                self.left = BinaryNode(value)
        else:
            if self.right is not None:
                self.right.insert_node(value)
            else:
                self.right = BinaryNode(value)


    def search_for_node(self, root, value):
        pass
