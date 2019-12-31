from collections import deque

"""Started with class-17 demo code and then added on to with lab partner, Charlie Glass"""

class BinaryTree:
    """BinaryTree"""

    def __init__(self):
        self._root = None

class BinarySearchTree():
    """BinarySearchTree with enough functionality for breadth first adding"""
    def __init__(self, value=None):
        self._root = value

    def add(self, value, current=None):
        
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


class _Node:
    """Protected Tree Node"""
    def __init__(self, value, left=None, right=None, next=None, previous=None):
        self.value = value
        self.left = left
        self.right = right
        self.next = next
        self.previous = previous


class Queue:
    """Implementation of Queue that "composes" built in deque class"""

    def __init__(self, front=None, previous=None):
        self.front = front
        self.previous = previous
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

    while q.front:
        node = q.front.value
        lst.append(node.value)

        if node.left:
            q.enqueue(node.left)

        if node.right:
            q.enqueue(node.right)

        q.dequeue()

    return lst

