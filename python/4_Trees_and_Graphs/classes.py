import random
from bst import BST

class BinaryTree(object):
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insertLeft(self, value):
        new_tree = BinaryTree(value)
        if self.left_child is None:
            self.left_child = new_tree
        else:
            new_tree.left_child = self.left_child
            self.left_child = new_tree

    def insertRight(self, value):
        new_tree = BinaryTree(value)
        if self.right_child is None:
            self.right_child = new_tree
        else:
            new_tree.right_child = self.right_child
            self.right_child = new_tree

    def __str__(self):
        return "[ {0} [ {1} | {2} ] ]".format(
                self.value, self.left_child, self.right_child)


class DirectedGraph(object):
    def __init__(self, content):
        self.content = content
        self.neighbors = []


class Queue(object):
    def __init__(self, data=None):
        self.first = None
        self.last = None
        self.length = 0
        if data:
            self.eq(data)

    def eq(self, data):
        if not self.first:
            self.last = Node(data)
            self.first = self.last
        else:
            newNode = Node(data)
            self.last.nextNode = newNode
            self.last = newNode
        self.length += 1

    def dq(self):
        assert self.first is not None, 'Queue is empty!'
        value = self.first.data
        self.first = self.first.nextNode
        self.length -= 1
        return value

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
    Builds a balanced binary tree recursively.
    """
    if depth == 0:
        return None
    tree = BinaryTree(random.randint(0, 100))
    tree.left_child = Balanced_BTree_Factory(depth - 1)
    tree.right_child = Balanced_BTree_Factory(depth - 1)
    return tree

