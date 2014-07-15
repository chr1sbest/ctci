"""
4.8

You have two very large binary trees: T1, with millions of nodes, and
T2, with hundreds of nodes. Create an algorithm to determine if T2 is 
a subtree of T1.

A tree is a subtree of T1 if there exists a node in T1 such that the
subtree of n is identical to T2. That is, if you cut off the tree at
node n, the two trees would be identical.
"""

def root_match(t1, t2):
    """
    Recursively check nodes of t1 for the root value of t2.
    If there is a match, check for equality.

    Time complexity: O(nm) WORST, but in practice closer to O(n).
    Space complexity: O(log(n) + log(m)) 
    """
    if t1.value == t2.value:    # Dive in and check if the trees match
        tree_match(t1, t2)
    else:                       # Recursively check children
        lchild, rchild = t1.left_child, t1.right_child
        return root_match(lchild, t2) or root_match(rchild, t2)

def tree_match(t1, t2):
    if not t1 and not t2:       # Both are empty
        return True
    elif bool(t1) != bool(t2):  # One has a value and other doesn't
        return False
    elif t1.data != t2.data:    # Values don't match
        return False
    else:                       # Recursively check children
        right_match = tree_match(t1.right_child, t2.right_child)
        left_match = tree_match(t1.left_child, t2.left_child)
        return right_match and left_match
