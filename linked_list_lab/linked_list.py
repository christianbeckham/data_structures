class Node:
    '''Represents a node.

    Attributes:
        value: The value assigned to the Node instance. Set during initialization.
        next: The following Node instance in a Linked List. Initally set to None or None if it is the tail.
    '''

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    '''Creates a new Linked List.

    Attributes:
        head: A Node instance representing the beginning of a Linked List. Initally set to None.
        tail: A Node instance representing the end of a Linked List. Initally set to None.
    '''

    def __init__(self):
        self.head = None
        self.tail = None

    def append_node(self, node_value):
        '''Adds a node to a linked list.

        Creates a new Node intance and sets the head, tail, and next instance variables.

        Args:
            node_value: The value assigned when creating a Node instance.

        Returns:
            None
        '''
        new_node = Node(node_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    def find_node(self, value):
        '''Find a node in a linked list.

        Returns a boolean if the value exists in the Linked List.

        Args:
            value: The value to check for in the Linked List.

        Returns:
            Boolean (True or False)
        '''
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False
