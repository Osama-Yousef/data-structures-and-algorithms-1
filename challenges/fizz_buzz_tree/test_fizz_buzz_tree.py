from fizz_buzz_tree import _Node, BinaryTree, fizz_buzz_tree
import pytest

@pytest.fixture
def empty_tree():

    return BinaryTree()

@pytest.fixture
def fizzy_tree():

    tree = BinaryTree()
    tree._root = _Node(3)
    tree._root.left = _Node(5)
    tree._root.right = _Node(7)
    tree._root.left.left = _Node(15)

    return tree

def test_empty_tree(empty_tree):
    '''Test that running fizz_buzz_tree on an empty tree returns an empty tree'''

    expected = None
    actual = fizz_buzz_tree(empty_tree)
    assert expected == actual._root
        
def test_fizz_buzz_filled_tree(fizzy_tree):
    '''
    Tests old_tree node values become fizz, buzz, str(num), 
    and fizzbuzz in new_tree node values
    '''

    new_tree = fizz_buzz_tree(fizzy_tree)
    assert new_tree._root.val == 'Fizz'
    assert new_tree._root.left.val == 'Buzz'
    assert new_tree._root.right.val == '7'
    assert new_tree._root.left.left.val == 'FizzBuzz'
