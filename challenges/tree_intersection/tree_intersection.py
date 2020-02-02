class _Node():
    '''BT specific node class.'''
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root=None):
        self.root = None
        output = []

    def get_root(self):
        return self.root

    def pre_order(self, output=output, node=None):
        if node == None:
            node = self.root
        output.append(node.val)

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
        if node.value in union:
            intersection.add(node.value)
        else:
            union.add(node.value)
        if node.right:
            walk(node.right, union, intersection)

    walk(left_tree.root)
    walk(right_tree.root)

    return intersection