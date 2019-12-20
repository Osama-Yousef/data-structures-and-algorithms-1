class _Node():
    def __init__(self, val, left=None, rht=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self._root = None

    def pre_order(self):
        pass

class BinarySearchTree(BinaryTree):
    def add(self, val):
        node = _Node(val)
        if not self._root:
            self._root = node
            return
        if val < self._root.value:
            if not self._root

            