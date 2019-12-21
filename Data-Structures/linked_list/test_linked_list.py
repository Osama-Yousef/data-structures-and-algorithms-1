# Can successfully instantiate an empty linked list
# Can properly insert into the linked list
# The head property will properly point to the first node in the linked list
# Can properly insert multiple nodes into the linked list
# Will return true when finding a value within the linked list that exists
# Will return false when searching for a value in the linked list that does not exist
# Can properly return a collection of all the values that exist in the linked list

from linked_list import Node, LinkedList
import pytest

def test_str():
    ll = LinkedList()
    ll.insert('blah1')
    ll.insert('blahblah')
    assert ll.__str__() == '{ blahblah } -> { blah1 } -> NULL'

def test_insert_first():
    """
    Can properly insert into the linked list
    """
    ll = LinkedList()
    ll.insert('blah')
    assert ll.head._data == 'blah'


def test_instantiate_linked_list():
    """
    Can successfully instantiate an empty linked list
    """
    ll = LinkedList()
    assert ll.head == None


def test_head_first():
    """
    The head property will properly point to the first node in the linked list
    """
    

def test_insert_multiple_nodes():
    """
    Can properly insert multiple nodes into the linked list
    """
    ll = LinkedList()
    ll.insert('blah1')
    ll.insert('blah2')
    assert ll.head._data == 'blah2'
    assert ll.head._next_node._data == 'blah1'

def test_found_value_true():
    """
    Will return true when finding a value within the linked list that exists
    """
    ll = LinkedList()
    ll.insert('blah1')
    ll.insert('blah2')
    assert ll.includes('blah1')

def test_found_value_false():
    """
    Will return false when searching for a value in the linked list that does not exist
    """
    ll = LinkedList()
    ll.insert('blah1')
    ll.insert('blah2')
    assert ll.includes('blah3') == False

def test_return_all_nodes():
    """
    Can properly return a collection of all the values that exist in the linked list
    """
    ll = LinkedList()
    ll.insert('blah1')
    ll.insert('blahblah')
    assert ll.__str__() == '{ blahblah } -> { blah1 } -> NULL'