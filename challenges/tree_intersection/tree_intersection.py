def tree_intersection(left_tree, right_tree):
    '''Take in two binary trees, return set of values found in both trees.'''

    # Elements from either sets (A) + (B)
    union = set()
    # Elements found only in both sets (A()B)
    intersection = set()

    if left_tree.root == None or right_tree.root == None:
        return intersection

    def walk(node, union=union, intersection=intersection):
        '''
        tree_intersection() helper function.
        Take in root node, union and intersection variables.
        Walk tree updating respective sets as we go.
        '''
        if node.left:
            walk(node.left, union, intersection)
        if node.data in union:
            intersection.add(node.data)
        else:
            union.add(node.data)
        if node.right:
            walk(node.right, union, intersection)

    walk(left_tree.root)
    walk(right_tree.root)

    return intersection