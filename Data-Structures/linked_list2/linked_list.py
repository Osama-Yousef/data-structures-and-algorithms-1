# Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
# Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.
# Define a method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
# Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
# Define a method called toString (or __str__ in Python) which takes in no arguments and returns a string representing all the values in the Linked List.

class Node:
    def __init__(self, e):
        self.e = e
        self.next = None

    def __repr__(self):
        return "Linked List Node"

class LinkedList:
    def __init__(self, e):
        self.e = e
        self.head = None

    def __repr__(self):
        return "Linked List"

    def __str__(self):
        """
        Define __str__ which takes in no arguments and returns a string
        representing all the values in the Linked List.
        """
        return 

    def insert(self, val):
        """
        Method called insert which takes any value as an argument 
        and adds a new node with that value to the head of the list
        with an O(1) Time performance.
        """
        node = Node(val)
        node.next = 

    def includes(self, e):
        """
        Define a method called includes which takes any value as an 
        rgument and returns a boolean result depending on whether that 
        value exists as a Node’s value somewhere within the list.
        """
        if self.e == e:
            return True
        else:
            return False
