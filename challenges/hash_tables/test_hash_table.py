# Retrieving based on a key returns the value stored
# Successfully returns null for a key that does not exist in the hashtable
# Successfully handle a collision within the hashtable
# Successfully retrieve a value from a bucket within the hashtable that has a collision


import pytest
from hash_table import HashTable

def test_hash_is_deterministic():
    '''Test that hash is deterministic i.e. that that same key will return the same index.'''
    ht = HashTable()
    actual = ht.hash('dog')
    assert actual == ht.hash('dog')
    assert 0 <= actual < 1024

def test_hash_add():
    '''Test that adding a key/value to your hashtable results in the value being in the data structure'''
    ht = HashTable()
    idx = ht.hash('dog')
    ht.add('dog','what ever you want')
    ll = ht.buckets[idx]
    key = ll.head._data.get('key')
    value = ll.head._data.get('value')
    assert 'dog' == key
    assert 'what ever you want' == value

def test_hash_get():
    '''Test that getting a key returns the value from the table.'''
    ht = HashTable()
    ht.add('dog','what ever you want')
    actual = ht.get('dog')
    assert actual == 'what ever you want'

def test_hash_get_value_not_present():
    '''Test that hash.get() raises errors correctly.'''
    with pytest.raises(KeyError):
        ht = HashTable()
        ht.get('dog')

