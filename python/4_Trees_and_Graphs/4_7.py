"""
4.7

Design an algorithm and write code to find the first common
ancestor of two nodes in a binary tree. Avoid storing additional
nodes in a data structure.

Note: This is not necessarily a BST.
"""

# Each node does not have a link to its parents.
def contains(root, target):
    """
    Recursively checks if the target node is a child of the root.
    """
    if not root:
        return False
    elif root is target:
        return True
    left, right = root.left_child, root.right_child
    return contains(left, target) or contains(right, target)

def ancestor_helper(root, node1, node2):
    if not root:                    
        # there is no match
        return False
    elif root is node1 or node2:    
        # one node is a child/grandchild of the other
        return root
    else:                           
        # recursively search the side that the nodes are on
        node1_left = contains(root.left_child, node1)
        node2_left = contains(root.left_child, node2)

        # return root if the nodes are on opposite sides of root
        if bool(node1_left) != bool(node2_left):
            return root
        # recursively traverse the side the children are on
        else:   
            child_side = root.left_child if node1_left else root.right_child
            return ancestor_helper(child_side, node1, node2)

def ancestor(root, node1, node2):
    n1_bool = contains(root, node1) #is node1 a child of the root?
    n2_bool = contains(root, node2) #is node2 a child of the root?
    if not n1_bool or not n2_bool:
        return False
    else:
        return ancestor_helper(root, node1, node2)
