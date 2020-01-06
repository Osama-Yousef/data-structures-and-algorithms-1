from collections import deque

"""Started with class-17 demo code and then added on to with lab partner, Charlie Glass"""

class BinaryTree:
    """BinaryTree with enough functionality for breadth first adding"""

    def __init__(self):
        self._root = None

    def add(self, value):

        node = _Node(value)

        if not self._root:
            self._root = node
            return

        q = Queue()

        q.enqueue(self._root)

        while not q.is_empty():

            current = q.dequeue()

            if current.left:
                q.enqueue(current.left)
            else:
                current.left = node
                break

            if current.right:
                q.enqueue(current.right)
            else:
                current.right = node
                break
    
    def find_maximum_value_recursive(self):
        """Recursive version - return the maximum value stored in the tree"""
        max_val = 0

        if not self._root:
            return max_val

        def _walk(node):
            '''Method to do heavy lifting.'''
            nonlocal max_val

            if node.value > max_val:
                max_val = node.value

            if node.left:
                _walk(node.left)

            if node.right:
                _walk(node.right)

        _walk(self._root)

        return max_val

    def find_maximum_value_iterative(self):
        '''Iterative version - return the maximum value stored in the tree'''
        
        max_val = 0

        if not self._root:
            return max_val

        queue = []
        queue.append(self._root)

        while queue:
            current_node = queue.pop(0)

            if type(current_node) != int:
                raise ValueError(f'{current_node} of type int only.')
            if current_node.value > max_val:
                max_val = current_node.value

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

        return max_val

class BinarySearchTree():
    """BinarySearchTree with enough functionality for breadth first adding"""
    def __init__(self, value=None):
        self._root = value

    def add(self, value, current=None):
        '''TODO: Create logic based on inclass psuedo code:
        https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-15/resources/Trees.html
        '''
        pass

# This node class is specific to trees!
class _Node:
    """Protected Tree Node. Of the binary tree variety."""
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left 
        self.right = right

class Queue:
    """Implementation of Queue that "composes" built in deque class"""

    def __init__(self):
        self._dq = deque()

    def enqueue(self, value):
        self._dq.appendleft(value)

    def dequeue(self):
        return self._dq.pop()

    def peek(self):
        return self._dq[-1]

    def is_empty(self):
        return len(self._dq) == 0

def breadth_first(tree):
    """
    Breadth first traversal that takes in binary tree, 
    traverses the tree using breadth first method and finally
    returns a list of the values in order    
    """

    if not tree._root:
        return None

    q = Queue()
    lst = []

    q.enqueue(tree._root)

    while not q.is_empty():
        node = q.dequeue()
        lst.append(node.value)

        if node.left:
            q.enqueue(node.left)

        if node.right:
            q.enqueue(node.right)

    return lst

