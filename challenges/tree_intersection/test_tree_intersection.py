from tree_intersection import _Node, BinaryTree, tree_intersection

def test_null_tree():
    '''Returns an empty set if either tree is null (empty)'''
    tree_a, tree_b = BinaryTree(), BinaryTree()
    actual = tree_intersection(tree_a, tree_b)
    expected = set()
    assert actual == expected

def test_node_creation():
    '''Test able to create node.'''
    node = _Node(88)
    actual = node.val
    assert actual == 88

def test_intersection():
    '''Test that given two BTs only elements found in both sets are returned.'''
    