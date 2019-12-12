
class Node:
    """Nonpublic class for storing a singly linked node"""
    def __init__(self, data, next_node = None):
        """Arguments passed to the class constructor expression"""
        self._data = data
        self._next_node = next_node

    def __repr__(self):
        """
        TODO: CONTENTS AND SYNTAX FOR REPR(). SEE PY3DOCS.
        https://docs.python.org/3/reference/datamodel.html#object.__repr__
        """
        return f"<class '__main__.Node: _data: {self._data} _next_node: {self._next_node}>"

    def __str__(self):
        """Nicely printable string representation of instantiated Node class"""
        return f"_data => {self._data} _next Node => {self._next_node}"

    def get_data(self):
        return self._data

    def get_next_node(self):
        return self._next_node

    def set_next_node(self, next_node):
        self._next_node = next_node

class LinkedList:
    """Singly linked list implementation"""
    def __init__(self):
        """Create empty linked list"""
        self.head = None
        self.size = 0

    def __len__(self):
        """Returns the number of elements in the stack"""
        return self.size

    def is_empty(self):
        """Returns True if the stack is empty"""
        return self.size == 0

    def __repr__(self):
        """TODO: SEE ABOVE. Returns printable representational string of the given object"""
        return f"<class '__main__.LinkedList: head: {self.head} size: {self.size}>"

    def __str__(self):
    #     """TODO: SEE ABOVE Returns a string representing all values on the stack"""
    #     Define a method __str__ 
    #     which takes in no arguments and returns a string representing all the values
    #     in the Linked List, formatted as:
    #     "{ a } -> { b } -> { c } -> NULL"
        current_node = self.head
        while current_node._next_node != None:
            print("{{ {} }} -> ".format(current_node), end='')
            current_node = current_node._next_node
        print("NULL")

    def insert(self, data):
        """PUSH a new node with that value to the head of the list with an O(1) time performance"""
        current_node = self.head
        self.head = Node(data, current_node)
        self.size += 1

    def includes(self, data):
        """Returns True if value exists on the stack"""
        current_node = self.head
        while current_node._next_node != None:
            if current_node._data == data:
                return True
            else:
                current_node = current_node._next_node

        return False
