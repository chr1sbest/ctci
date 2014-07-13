import random

class BinaryTree(object):
    def __init__(self, root):
        self.root = root
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
                self.root, self.left_child, self.right_child)

class BST(object):
    def __init__(self, key=None, value=None, parent=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left_child = None
        self.right_child = None

    def insert(self, key, value):
        if self.key == None:
            self.key, self.value = key, value
        elif self.key == key:
            self.value = value
        elif self.key < key:
            if not self.left_child: 
                self.left_child = BST(key, value, self)
            else:
                self.left_child.insert(key, value, self)
        else:
            if not self.right_child: 
                self.right_child = BST()
            else:
                self.right_child.insert(key, value, self)

    def search(self, key):
        if self.key == key:
            return self
        elif key < self.key:
            return self.left_child.search(key)
        elif key > self.key:
            return self.right_child.search(key)
        else:
            return False

    def which_branch(self):
        if self.parent.left_child == self:
            return 'left'
        elif self.parent.right_child == self:
            return 'right'
        else: # No children
            return None

    def delete(self, key):
        """
        Remove a node from the BST.
        """
        node = self.search(key)
        child_branch = node.which_branch() # left or right child of parent?

        # Case 1, searched node is leaf with no children
        if not node.left_child and not node.right_child:
            if child_branch == 'left':
                node.parent.left_child = None
            elif child_branch == 'right':
                node.parent.right_child = None
            else:
                node.value, node.key = None, None

        # Case 2, node has a single child
        elif bool(node.left_child) != bool(node.right_child):
            if node.left_child: # Replace self with left child
                node.left_child.parent = node.parent
                if child_branch == 'left':
                    node.parent.left_child = node.left_child
                elif child_branch == 'right':
                    node.parent.right_child = node.left_child
                else:
                    node = node.left_child
            else: # Replace self with right child
                node.right_child.parent = node.parent
                if child_branch == 'left':
                    node.parent.left_child = node.right_child
                elif child_branch == 'right':
                    node.parent.right_child = node.right_child
                else:
                    node = node.right_child

        # Case 3, node has two children
        else:
            successor = node.find_successor()
            successor.splice_out()

    def find_successor(self):
        """
        Find the element that has the next highest key after self.
        """
        successor = None
        if self.right_child:
            successor = self.right_child.find_min()
        else:
            if self.parent and self.which_branch() == 'left':
                successor = self.parent
            elif self.parent and self.which_branch() == 'right':
                self.parent.right_child = None
                self.parent.find_successor()
                self.parent.right_child = self
        return successor

    def find_min(self):
        """
        Find deepest left child.
        """
        current = self
        while current.left_child:
            current = current.left_child
        return current

    def splice_out(self):
        if not self.left_child and not self.right_child:
            if self.which_child() == 'left':
                self.parent.left_child = None
            elif self.which_child() == 'right':
                self.parent.right_child = None
        elif bool(self.left_child) != bool(self.right_child):


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

