class BinaryNode:
    '''Represents a node element in a tree.

    Attributes:
        data: The value assigned to the node. Set during initialization.
        left: The child node with a value less than the parent node. Initally set to None.
        right: The child node with a value greater than the parent node. Initally set to None.
    '''

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert_node(self, value):
        '''Insert a node in the tree.

        Creates a new node intance and inserts it at the appropriate level. 
        If the value is less than the parent, the node is assigned to the left instance variable.
        If the value is greater than the parent, the node is assigned to the right instance variable.

        Args:
            value: The value of the node to insert.

        Returns:
            None
        '''
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

    def search_for_node(self, node, value):
        '''Find a node in the tree.

        Searches the left or right instance variables of a node to find the value.
        If the value is less than the node, searching will shift to the left of the tree.
        If the value is greater than the node, searching will shift to the right of the tree.

        Args:
            node: A BinaryNode instance.
            value: The value of the node to search for.

        Returns:
            None
        '''
        if node is None:
            print('Node not found!')
            return

        if node.data == value:
            print('Node found!')
            return
        elif node.data > value:
            print('Direction left')
            node.search_for_node(node.left, value)
        else:
            print('Direction right')
            node.search_for_node(node.right, value)

    def inorder_traversal(self, node, order=[]):
        '''Inorder (Left, Root, Right)
        '''

        if node is not None:
            self.inorder_traversal(node.left)
            order.append(node.data)
            self.inorder_traversal(node.right)
        return order

    def preorder_traversal(self, node, order=[]):
        '''Preorder (Root, Left, Right)
        '''
        if node is not None:
            order.append(node.data)
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)
        return order

    def postorder_traversal(self, node, order=[]):
        '''Postorder (Left, Right, Root)
        '''
        if node is not None:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            order.append(node.data)
        return order
