from find_maximum_value import _Node, BinaryTree, BinarySearchTree, breadth_first

def test_empty_tree():
    '''If tree._root is None return None.'''
    tree = BinarySearchTree()
    actual = breadth_first(tree)
    expected = None
    assert expected == actual

def test_single_node():
    '''Test that binary tree with single item returns list with that single item.'''
    tree = BinaryTree()
    tree.add(15)
    actual = breadth_first(tree)
    expected = [15]
    assert expected == actual

def test_four_nodes():
    '''Test that binary tree with four nodes returns list with those four items.'''
    tree = BinaryTree()
    tree.add(11)
    tree.add(9)
    tree.add(15)
    tree.add(5)
    actual = breadth_first(tree)
    expected = [11, 9, 15, 5]
    assert expected == actual 


def test_many_nodes():
    '''Test that binary tree with 10 nodes returns list with those 10 items.'''
    tree = BinaryTree()
    tree.add(11)
    tree.add(9)
    tree.add(15)
    tree.add(5)
    tree.add(11)
    tree.add(9)
    tree.add(15)
    tree.add(5)
    actual = breadth_first(tree)
    expected = [11, 9, 15, 5, 11, 9, 15, 5]
    assert expected == actual

def test_return_max_single_node():
    '''Test that binary tree with single item returns correct value.'''
    tree = BinaryTree()
    tree.add(15)
    actual_iterative = tree.find_maximum_value_iterative()
    actual_recursive = tree.find_maximum_value_recursive()
    expected = [15]
    assert actual_iterative == 15
    assert actual_recursive == 15

def test_return_maxVal_of_all():
    '''Test that binary tree with many nodes returns correct value.'''
    tree = BinaryTree()
    tree.add(11)
    tree.add(9)
    tree.add(15)
    tree.add(5)
    tree.add(11)
    tree.add(9)
    tree.add(15)
    tree.add(5)
    actual_iterative = tree.find_maximum_value_iterative()
    actual_recursive = tree.find_maximum_value_recursive()
    assert actual_iterative == 15
    assert actual_recursive == 15

def test_no_string():
    '''Test that binary tree with many nodes returns exception if given non-numeric value.'''
    tree = BinaryTree()
    tree.add('string_cheese')
    actual_iterative = tree.find_maximum_value_iterative()
    actual_recursive = tree.find_maximum_value_recursive()
    assert actual_iterative == 15
    assert actual_recursive == 15

def test_max_of_none():
    '''test_max_of_none - If tree._root is None return None.'''
    tree = BinaryTree()
    actual_iterative = tree.find_maximum_value_iterative()
    actual_recursive = tree.find_maximum_value_recursive()

    assert actual_iterative == 0
    assert actual_recursive == 0

