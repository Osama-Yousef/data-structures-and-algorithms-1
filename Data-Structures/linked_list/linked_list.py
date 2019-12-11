
class Node:
    """Nonpublic class for storing a singly linked node"""
    def __init__(self, element, next = None):
        """Arguments passed to the class constructor expression"""
        self._element = element
        self._next = next

    def __repr__(self):
        """
        TODO: CONTENTS AND SYNTAX FOR REPR(). SEE PY3DOCS.
        https://docs.python.org/3/reference/datamodel.html#object.__repr__
        """
        return "<class '__main__.Node: {self._element} {self._next}>"

    def __str__(self):
        """
        TODO: MAKE THIS.“informal” or nicely printable string representation of an object.
        https://docs.python.org/3/reference/datamodel.html#object.__str__
        """

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
        return self

    # def __str__(self):
    #     """TODO: SEE ABOVE Returns a string representing all values on the stack"""
    #     Define a method __str__ 
    #     which takes in no arguments and returns a string representing all the values
    #     in the Linked List, formatted as:
    #     "{ a } -> { b } -> { c } -> NULL"

    def insert(self, e):
        """PUSH a new node with that value to the head of the list with an O(1) time performance"""
        self.head = Node(e, self.head)
        self.size += 1

    # def includes(self, e):
    #     """Returns True if value exists on the stack"""
    #     if self.e == e:
    #         return True
    #     else:
    #         return False
