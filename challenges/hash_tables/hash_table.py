from linked_list import LinkedList

class HashTable:
    def __init__(self):
        '''No default inputs.'''
        self.buckets = [None] * 1024

    def add(self, key, value):
        '''Hashes key, adds key and value pair to table. Handles collisions as necessary.'''

        index = self.hash(key)
        if self.buckets[index] == None:
            bucket = LinkedList()
        else:
            bucket = self.buckets[index]    # bucket is now a linked list
        
        bucket.insert(
            {
                'key': key,
                'value': value,
            }
        )
        
        self.buckets[index] = bucket

    def get(self, key):
        '''Takes in key and returns the value from the table. Handles collisions as necessary.'''
        idx = self.hash(key)
        # bucket is the element, and bucket is either None or LL.
        bucket = self.buckets[idx]
        if bucket == None:
            raise KeyError('Key not present in hash table')
        current = bucket.head
        while current:
            if current._data['key'] == key:
                return current._data['value']
            current = current._next_node
        
        # We walked entire ll and didn't find key
        raise KeyError('Key not present in hash table')

    def contains(self, key):
        '''Takes in the key and returns a boolean, indicating if the key exists in the table already.'''
        idx = self.hash(key)
        # bucket is the element, and bucket is either None or LL.
        bucket = self.buckets[idx]
        if bucket == None:
            return False
        current = bucket.head
        while current:
            if current._data['key'] == key:
                return True
            current = current._next_node
        
        # We walked entire ll and didn't find key
        return False

    def hash(self, key):
        '''Takes in an arbitrary key and returns an index in the collection.'''
        # Algo
        # - Add or multiply all the ASCII values together.
        # - Multiply it by a prime number such as 599.
        # - Use modulo to get the remainder of the result, when divided by the total size of the array.
        # - Insert into the array at that index.
        prime_value = 599
        hashed_key = sum([ord(char) for char in key]) * prime_value
        hashed_key = hashed_key % 1024

        return hashed_key
  