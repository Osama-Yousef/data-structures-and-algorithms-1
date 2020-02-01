# add: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
# get: takes in the key and returns the value from the table.
# contains: takes in the key and returns a boolean, indicating if the key exists in the table already.
# hash: takes in an arbitrary key and returns an index in the collection.

class HashTable:
    def __init__(self):
        '''No default inputs.'''
        bucket = [None] * 1024

    def add(self, key, value):
        '''TODO: Hashes key, adds key and value pair to table. Handles collisions as necessary.'''
        self.key = key
        self.value = value

    def get(self, key):
        '''TODO: Takes in key and returns the value from the table.'''
        self.key = key
        self.value = value
        pass

    def contains(self, key):
        '''TODO: Takes in the key and returns boolean, indicating if the key exists in the table already.'''
        self.key = key
        pass

    def hash(self, key):
        '''TODO: Takes in an arbitrary key and returns an index in the collection.'''
        # Algo
        # - Add or multiply all the ASCII values together.
        # - Multiply it by a prime number such as 599.
        # - Use modulo to get the remainder of the result, when divided by the total size of the array.
        # - Insert into the array at that index.
        prime_value = 599
        hashed_key = sum([ord(char) for char in key]) * prime_value
        hashed_key = hashed_key % 1024

        return hashed_key
        

    