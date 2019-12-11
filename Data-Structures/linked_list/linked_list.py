# Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
# Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.
# Define a method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
# Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
# Define a method called toString (or __str__ in Python) which takes in no arguments and returns a string representing all the values in the Linked List.

class _Node:
    """Nonpublic class for storing a singly linked node"""
    def __init__(self, element, next=None):
        """Arguments passed to the class constructor expression"""
        self._element = element
        self._next = next

    def __repr__(self):
        """
        TODO: CONTENTS AND SYNTAX FOR REPR(). SEE PY3DOCS.
        https://docs.python.org/3/reference/datamodel.html#object.__repr__
        """
        return "<class '__main__._Node: {self._element} {self._next}>"

    def __str__(self):
        """
        TODO: MAKE THIS.“informal” or nicely printable string representation of an object.
        https://docs.python.org/3/reference/datamodel.html#object.__str__
        """

class LinkedList:
    """Singly linked list implementation"""
    def __init__(self):
        """Create empty linked list"""
        self._head = None
        self._size = 0

    def __len__(self):
        """Returns the number of elements in the stack"""
        return self._size

    def is_empty(self):
        """Returns True if the stack is empty"""
        return self._size == 0

    def __repr__(self):
        """TODO: SEE ABOVE. Returns printable representational string of the given object"""
        return repr(self)

    # def __str__(self):
    #     """TODO: SEE ABOVE Returns a string representing all values on the stack"""
    #     Define a method __str__ 
    #     which takes in no arguments and returns a string representing all the values
    #     in the Linked List, formatted as:
    #     "{ a } -> { b } -> { c } -> NULL"

    def insert(self, e):
        """PUSH a new node with that value to the head of the list with an O(1) time performance."""
        self._head = _Node(e, self._head)
        self._size += 1

    # def includes(self, e):
    #     """Returns True if value exists on the stack"""
    #     if self.e == e:
    #         return True
    #     else:
    #         return False
