"""
4.4

Given a binary tree, design an algorithm which creates a linked list
of all the nodes at each depth.
"""
from classes import LinkedList, BinaryTree, Node

def listmaker(current_node, depth=0, cache={}):
    if cache[depth]:
        cache[depth].next_node = Node(current_node.value)
    else:
        cache[depth] = LinkedList(current_node.value)
    if current_node.left_child:
        listmaker(current_node.left_child, depth + 1, cache)
    if current_node.right_child:
        listmaker(current_node.right_child, depth + 1, cache)
    return cache
