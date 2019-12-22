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

def test_append():
    """
    Can successfully add a node to the end of the linked list
    """
    ll = LinkedList()
    ll.append('blah')
    assert ll.head._data == 'blah'

def test_add_multiple_append():
    """
    Can successfully add multiple nodes to the end of a linked list
    """
    ll = LinkedList()
    ll.append('blah')
    ll.append('blah2')
    assert ll.head._data == 'blah'
    assert ll.head._next_node._data == 'blah2'

def test_insert_before_middle():
    """
    Can successfully insert a node before a node located in the middle of a linked list
    """
    ll = LinkedList()
    ll.append('blah1')
    ll.append('blah2')
    ll.append('blah3')
    ll.insert_before('blah2', 33)
    assert ll.head._next_node._data == 33
    
def test_insert_before_first_node():
    """
    Can successfully insert a node before the first node of a linked list
    """
    ll = LinkedList()
    ll.append('blah1')
    ll.insert_before('blah1', 22)
    assert ll.head._data == 22

def test_insert_after_after_middle():
    """
    Can successfully insert after a node in the middle of the linked list
    """
    ll = LinkedList()
    ll.append('blah1')
    ll.append('blah2')
    ll.append('blah3')
    ll.insert_after('blah2', 33)
    assert ll.head._next_node._next_node._data == 33   

def test_insert_after_last():
    """
    Can successfully insert a node after the last node of the linked list
    """
    ll = LinkedList()
    ll.append('blah1')
    ll.append('blah2')
    ll.append('blah3')
    ll.insert_after('blah3', 33)
    assert ll.head._next_node._next_node._next_node._data == 33

#
# Class 07 - kth_from_end
#
def test_kth_greater_than_list_length():
    '''
    Successfully handle where k is greater than the length of the linked list
    '''
    ll = LinkedList()
    ll.append('blah1')
    with pytest.raises(ValueError):
        ll.kth_from_end(2)

def test_kth_equal_to_list_length():
    '''Where k and the length of the list are the same'''
    ll = LinkedList()
    ll.append('blah1')
    with pytest.raises(ValueError):
        ll.kth_from_end(1)

def test_k_not_positive_integer():
    '''Where k is not a positive integer'''
    ll = LinkedList()
    ll.append('blah1')
    with pytest.raises(ValueError):
        ll.kth_from_end(-3)

def test_linked_list_has_single_node():
    ''' Where the linked list is of a size 1'''
    ll = LinkedList()
    ll.append('blah1')
    assert ll.kth_from_end(0) == 'blah1'

def test_middle_k():
    """
    “Happy Path” where k is not at the end, but 
    somewhere in the middle of the linked list
    """
    ll = LinkedList()
    ll.append('blah1')
    ll.append('blah2')
    ll.append('blah3')
    ll.append('blah4')
    ll.append('blah5')
    ll.append('blah6')
    assert ll.kth_from_end(3) == 'blah3'