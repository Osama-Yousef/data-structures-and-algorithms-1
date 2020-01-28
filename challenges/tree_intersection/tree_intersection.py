def tree_intersection(left_tree, right_tree):
    '''Take in two binary trees, return set of values found in both trees.'''

    if left_tree == None or right_tree == None:
        return

    touched = set()
    overlap = set()

    def walk(node):
        nonlocal touched

        touched.add(node.value)
        walk(node.left)
        walk(node.right)

    def walk_other(node):
        nonlocal touched
        nonlocal overlap

        if node.value in touched:
            overlap.add(node.value)

        walk(node.left)
        walk(node.right)

    walk(left_tree.root)
    walk_other(right_tree.root)

    return overlap
