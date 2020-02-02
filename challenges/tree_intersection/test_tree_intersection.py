from tree_intersection import tree_intersection
from tree import BinaryTree, BinarySearchTree
import pytest

@pytest.fixture
def tree_a():
    tree = BinarySearchTree(88)
    tree.add(66)
    tree.add(60)
    tree.add(55)
    tree.add(50)
    tree.add(40)

    return tree

@pytest.fixture
def tree_b():
    tree = BinarySearchTree(1000)
    tree.add(900)
    tree.add(850)
    tree.add(800)
    tree.add(50)
    tree.add(40)

    return tree

def test_null_tree():
    ''' Returns an empty set if either tree is null (empty) '''
    tree_a, tree_b = BinaryTree(), BinaryTree()
    actual = tree_intersection(tree_a, tree_b)
    expected = set()
    assert actual == expected

def test_intersection(tree_a, tree_b):
    ''' Test that given two BTs only elements found in both sets are returned. '''
    assert tree_intersection(tree_a, tree_b) == {50,40}