"""
4.3

Given a sorted array with unique integer elements, write an algorithm to create
a binary search tree with minimum height
"""
from classes import BinaryTree

def array_to_tree(array):
    """
    Recursively build a tree, each with a smaller element on the left and
    larger element on the right.
    """
    if not array:
        return None
    mid = (len(array)) / 2
    root = TreeNode(array[mid])
    root.left_child = array_to_tree(array[:mid])
    root.right_child = array_to_tree(array[mid + 1:])
    return root


