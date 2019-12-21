class Node:
    '''
    Doubly linked Node (Generic Pet Construct)
    '''
    def __init__(self, pet_type, prev, next):
        self.pet_type = pet_type
        self.next = next
        self.prev = prev
    
class AnimalShelter:
    '''
    FIFO based class which holds only dogs and cats.
    The shelter operates using a first-in, first-out approach.
    '''

    def __init__(self):
        '''Creates an empty list to start'''
        self._head = Node(None, None, None)
        self._tail = Node(None, None, None)
        self._head.next = self._tail
        self._tail.prev = self._head
        self._size = 0

    def __len__(self):
        '''Return number of elements in the queue'''
        return self._size

    def is_empty(self):
        '''Return True if list is empty'''
        return self._size == 0

    def __str__(self):
        '''TODO: '''

    def __repr__(self):
        '''TODO'''

    def enqueue(self, pet_type, predecessor, successor):
        '''TODO: Add animal to the shelter. Only takes cat or dog objects.'''
        newest = Node(pet_type, predecessor, successor)
        predecessor.next = successor
        successor.next = newest
        self._size += 1
        return newest

    def dequeue(self, node):
        '''
        TODO: Currently only returns head node! 
        Walk back from head to tail node
        to first node matching request. If pref is not "dog" or "cat"
        return head node
        '''
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self._size -= 1
        pet_type = node.pet_type
        node.prev = node.next = node.pet_type = None
        return pet_type
