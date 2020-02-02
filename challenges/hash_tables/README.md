# Code Challenge - Hash Tables

Implement a hash table with the methods listed under Challenge.

## Tests

- test_hash_is_deterministic - Test that hash is deterministic i.e. that that same key will return the same index.'''
- test_hash_add - Test that adding a key/value to your hashtable results in the value being in the data structure'''
- test_hash_get - Test that getting a key returns the value from the table.
- test_hash_get_value_not_present - Test that hash.get() raises errors correctly.
- test_hash_handles_collisions - Test that key collisions are handled properly.
- test_hash_contains - Test that contains() returns Boolean representing if key is present.

## Challenge

Implement a Hashtable with the following methods:

- add: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
- get: takes in the key and returns the value from the table.
- contains: takes in the key and returns a boolean, indicating if the key exists in the table already.
- hash: takes in an arbitrary key and returns an index in the collection.

## Approach & Efficiency

## API

- add: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
- get: takes in the key and returns the value from the table.
- contains: takes in the key and returns a boolean, indicating if the key exists in the table already.
- hash: takes in an arbitrary key and returns an index in the collection.

## Big O notation

- time <- O(1)
- space <- O(1)

## Solution

[Implementation](hash_table.py)
[Test Implementation](test_hash_table.py)
