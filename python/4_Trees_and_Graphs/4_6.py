"""
4.6

Write an algorithm to find the next node of a given node
in a binary search tree. You may assume each node has a link
to its parent.
"""

class BST_Mixin_Next_Node(object):
    """
    Mixin that gives BST the ability to determine the next highest node.
    """
    def which_branch(self):
        if self.parent.left_child == self:
            return 'left'
        elif self.parent.right_child == self:
            return 'right'
        else: # No children
            return None

    def find_successor(self):
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

