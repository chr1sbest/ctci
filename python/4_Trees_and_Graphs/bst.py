BST_Mixin_Next_Node = __import__('4_6').BST_Mixin_Next_Node 

class BST(BST_Mixin_Next_Node):
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

    def splice_out(self):
        if not self.left_child and not self.right_child:
            if self.which_child() == 'left':
                self.parent.left_child = None
            elif self.which_child() == 'right':
                self.parent.right_child = None
        elif bool(self.left_child) != bool(self.right_child):
            pass


    def __iter__(self):
        if self:
            if self.left_child:
                yield self.left_child.key
            yield self.key
            if self.right_child:
                yield self.right_child.key


    @property
    def size(self):
        if not self.left_child and not self.right_child:
            return 1
        elif self.left_child and self.right_child:
            return self.left_child.size + self.right_child.size
        else:
            if self.left_child:
                return self.left_child.size + 1
            else:
                return self.right_child.size + 1
