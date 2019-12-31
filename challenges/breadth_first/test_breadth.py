from breadth import _Node, BinaryTree, BinarySearchTree, breadth_first

def test_empty_tree():
    '''If tree._root is None return None.'''
    tree = BinarySearchTree()
    actual = breadth_first(tree)
    expected = None
    assert expected == actual

def test_single_node():
    '''Test that binary tree with single item returns list with that single item.'''
    pass

def test_four_nodes():
    '''Test that binary tree with four nodes returns list with those four items.'''
    pass


def test_many_nodes():
    '''Test that binary tree with 10 nodes returns list with those 10 items.'''
    pass