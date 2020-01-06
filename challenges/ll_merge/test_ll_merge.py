from linked_list import LinkedList, Node
from ll_merge import merge_lists
import pytest

@pytest.fixture
def even_lists():
    '''Even Lists'''
    ll_1 = LinkedList()
    ll_1.append('blah1')
    ll_1.append('blah3')
    ll_1.append('blah5')
    ll_1.append('blah7')
    ll_1.append('blah9')
    ll_1.append('blah11')
    ll_2 = LinkedList()
    ll_2.append('blah2')
    ll_2.append('blah4')
    ll_2.append('blah6')
    ll_2.append('blah8')
    ll_2.append('blah10')
    ll_2.append('blah12')
    return ll_1, ll_2
    
def test_lists_of_equal_size(even_lists):
    '''Test for lists of equal size zipper correctly'''
    ll_1, ll_2 = even_lists
    actual = merge_lists(ll_1, ll_2)
    assert actual._data == 'blah1'
    assert actual._next_node._data == 'blah2'

@pytest.fixture
def uneven_lists():
    ll_1 = LinkedList()
    ll_1.append('blah1')
    ll_1.append('blah3')
    ll_1.append('blah5')
    ll_1.append('blah7')
    ll_1.append('blah9')
    ll_1.append('blah11')
    ll_2 = LinkedList()
    ll_2.append('blah2')

    return ll_1, ll_2

def test_list1_is_longer(uneven_lists):
    ll_1, ll_2 = uneven_lists
    actual = merge_lists(ll_1, ll_2)
    assert actual._data == 'blah1'
    assert actual._next_node._next_node._next_node._data == 'blah5'

def test_list2_is_longer(uneven_lists):
    ll_2, ll_1 = uneven_lists
    actual = merge_lists(ll_1, ll_2)
    assert actual._data == 'blah2'
    assert actual._next_node._data == 'blah1'
    assert actual._next_node._next_node._next_node._data == 'blah5'
