"""
4.5

Implement a function to check if a binary tree is a BST
"""

def bst_check(tree, min_val=None, max_val=None):
    if not min_val and not max_val:
        min_val, max_val = tree.value, tree.value

    if not tree:
        return True
    elif tree.value not in range(min_val + 1, max_val - 1):
        return False
    else:
        left = bst_check(left_child, min_val, tree.value)
        right = bst_check(right_child, tree.value, max_val)
        return left and right
