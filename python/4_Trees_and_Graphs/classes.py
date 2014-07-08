import random

class BinaryTree(object):
    def __init__(self, root):
        self.root = root
        self.left_child = None
        self.right_child = None

    def insertLeft(self, value):
        leaf = BinaryTree(value)
        if self.left_child is None:
            self.left_child = leaf
        else:
            leaf.left_child = self.left_child
            self.left_child = leaf

    def insertRight(self, value):
        leaf = BinaryTree(value)
        if self.right_child is None:
            self.right_child = leaf
        else:
            leaf.right_child = self.right_child
            self.right_child = leaf

    def __str__(self):
        return "[ {0} [ {1} | {2} ] ]".format(
                self.root, self.left_child, self.right_child)


def BTree_Factory(values):
    """
    Builds and randomly adds values to left/right nodes in a binary tree.
    """
    bt = BinaryTree(values[0])
    for val in values[1:]:
        if random.choice([True, False]):
            bt.insertLeft(val)
        else:
            bt.insertRight(val)
    return bt

def Balanced_BTree_Factory(depth):
    """
    Builds a balanced binary tree recursively
    """
    if depth == 0:
        return None
    tree = BinaryTree(random.randint(0, 100))
    tree.left_child = Balanced_BTree_Factory(depth - 1)
    tree.right_child = Balanced_BTree_Factory(depth - 1)
    return tree

