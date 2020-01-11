
class _Node():
    '''add comment'''
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    '''add comment'''
    def __init__(self):
        self._root = None

    def pre_order(self):
        pass

    def in_order(self):
        pass

    def post_order(self):
        pass

    def contains(self):
        pass

    def is_empty(self):
        pass

def fizz_buzz_tree(tree):
    new_tree = BinaryTree()
    new_node = _Node()

    if tree._root == None:
        return new_tree
        
    old_node = tree._root   # _root is ref to first node



    def visit_node(old_node, new_node):
        '''define'''
        new_node.val = fizz_buzz(old_node.val)
        if old_node.left:
            new_node.left = _Node()
            visit_node(old_node.left, new_node.left)

        if old_node.right:
            new_node.right = _Node()
            visit_node(old_node.right, new_node.right)

    def fizz_buzz(old_value):
        '''define'''
        result = ''
        if old_value % 3 == 0:
            result += 'Fizz'

        if old_value % 5 == 0:
            result += 'Buzz'

        return result or str(old_value)

    visit_node(old_node, new_node)

    new_tree._root = new_node

    return new_tree




