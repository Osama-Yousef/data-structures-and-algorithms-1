# Adding a key/value to your hashtable results in the value being in the data structure
# Retrieving based on a key returns the value stored
# Successfully returns null for a key that does not exist in the hashtable
# Successfully handle a collision within the hashtable
# Successfully retrieve a value from a bucket within the hashtable that has a collision
# Successfully hash a key to an in-range value

import pytest
from hash_table import HashTable

def test_hash_is_deterministic():
    '''Test that hash is deterministic i.e. that that same key will return the same index.'''
    ht = HashTable()
    actual = ht.hash('dog')
    assert actual == ht.hash('dog')
    assert 0 <= actual < 1024