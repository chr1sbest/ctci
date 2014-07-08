"""
4.1

Implement a function to check if a binary tree is balanced. For the purposes
of this question, a balanced tree is definted to be a tree such that the
heights of the two subtrees of any node never differ than more than one.
"""
from classes import BinaryTree, BTree_Factory, Balanced_BTree_Factory

def abs(value):
    return value if value > 0 else 0 - value

# Naive solution
def is_balanced(root):
    """
    Check if trees are balanced by recursing through the entire tree to check
    if any subtree's branch height differs by more than 1.

    Time complexity: O(nlogn)
    """
    if root is None:
        return True
    difference = abs(get_height(root.left_child) - get_height(root.right_child))
    if difference > 1:
        return False
    else:
        return is_balanced(root.left_child) and is_balanced(root.right_child)

def get_height(root):
    if root is None:
        return 0
    else:
        return max(get_height(root.left_child), get_height(root.right_child)) + 1


# Improved Solution
def is_balanced2(root):
    """
    Check if trees are balanced by recursing through the entire tree to check
    if any subtree's branch height differs by more than 1.

    Breaks and immediately returns -1 if any subtree is unbalanced.

    Time complexity: O(n)
    Space complexity: O(h) where h is the height of the tree
    """
    return False if check_height(root) == -1 else True

def check_height(root):
    if root is None:
        return 0

    # Check if left and right are balanced
    lheight = check_height(root.left_child)
    rheight = check_height(root.right_child)
    if lheight == -1 or rheight == -1:
        return -1

    # Check if current node is balanced
    diff = abs(lheight - rheight)
    return -1 if diff > 1 else max(lheight, rheight) + 1


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5, 6]
    unbalanced = BTree_Factory(values)
    balanced = Balanced_BTree_Factory(3)
    print "M1. Unbalanced is balanced? {0}".format(is_balanced(unbalanced))
    print "M1. Unbalanced is balanced? {0}".format(is_balanced2(unbalanced))
    print "M2. Balanced is balanced? {0}".format(is_balanced(balanced))
    print "M2. Balanced is balanced? {0}".format(is_balanced2(balanced))
