
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

class LinkedList:
    """Singly linked list implementation"""
    def __init__(self, value = None):
        """Create empty linked list"""
        self.head = value
        self.size = 0

    def __len__(self):
        """Returns the number of elements in the stack"""
        return self.size

    def is_empty(self):
        """Returns True if the stack is empty"""
        return self.size == 0

    def __repr__(self):
        """Returns printable representational string of the given object"""
        return f"<class '__main__.LinkedList: head: {self.head} size: {self.size}>"

    def __str__(self):
        """Returns a string representing all values on the stack"""
        current_node = self.head
        result = ''
        while current_node:
            result += f'{{ {current_node._data} }} -> '
            current_node = current_node._next_node
        result += f'NULL'
        return result

    def insert(self, data):
        """PUSH a new node with that value to the head of the list with an O(1) time performance"""
        current_node = self.head
        self.head = Node(data, current_node)
        self.size += 1

    def includes(self, data):
        """Returns True if value exists on the stack"""
        current_node = self.head
        while current_node:
            if current_node._data == data:
                return True
            else:
                current_node = current_node._next_node

        return False

    def append(self, value):
        '''Adds a new node with the given value to the end of the list'''
        node = Node(value)
        current_node = self.head
        if not self.head:
            self.head = node
            return 
        while current_node:
            if current_node._next_node == None:
                current_node._next_node = node
                return
            else:
                current_node = current_node._next_node
            
    def insert_before(self, value, new_val):
        '''Add a new node with the given newVal immediately before the first value node'''
        node = Node(new_val)
        current_node = self.head
        while current_node:
            if current_node._data == value:
                node._next_node = current_node
                self.head = node
                return
            if current_node._next_node:
                if current_node._next_node._data == value:
                    node._next_node = current_node._next_node
                    current_node._next_node = node
                    return
                current_node = current_node._next_node
        raise ValueError(f'{value} not found')
    
    def insert_after(self, value, new_val):
        '''Add a new node with the given newVal immediately after the first value node'''
        node = Node(new_val)
        current_node = self.head
        while current_node:
            if current_node._data == value:
                node._next_node = current_node._next_node
                current_node._next_node = node
                return
            current_node = current_node._next_node
        raise ValueError(f'{value} not found')

    def kth_from_end(self, k):
        '''Returns the node’s value that is k from the end'''
        if k < 0:
            raise ValueError(f'{k} is a negative value')
        if k == 0:
            if self.head:
                return self.head._data
        leader = self.head
        follower = self.head
        incrementer = 0
        while leader._next_node:
            leader = leader._next_node
            incrementer += 1
            if incrementer > k:
                follower = follower._next_node
        if k >= incrementer:
            raise ValueError(f'{k} exceeds length of list')
        return follower._data
