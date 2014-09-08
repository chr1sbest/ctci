def BST_gca(root, val1, val2):
    """
    Determine lowest common ancestor of two nodes in a BST.

    Time Complexity: O(h) -> Height of the BST
    """
    if root.data < val1 and root.data < val2:
        gca(root.left_child, val1, val2)
    elif root.data > val1 and root.data > val2:
        gca(root.right_child, val1, val2)
    elif val1 < root.data < val2 or val2 < root.data < val1:
        return root
    else:
        return False

