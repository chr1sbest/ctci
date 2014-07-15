"""
4.9

You are given a binary tree in which each node contains an integer
value (which might be positive or negative. Design an algorithm to
print all paths which sum to a given value. The path does not need
to start or end at the root or a leaf, but it must go straight down.
"""
from copy import copy
from classes import BinaryTree

def path_finder(tree, value, level=0, path=[]):
    if not tree:
        return
    if len(path) > level:
        path[level] = tree.value
    else:
        path.append(tree.value)
    
    if sum(path) == value:          #path adds to target value
        print path
    reversed_path = path[::-1]      #check paths from leaf upwards
    for index, val in enumerate(reversed_path):
        if sum(reversed_path[:index]) == value:
            print reversed_path[:index]

    path_finder(tree.left_child, value, level + 1, path)
    path_finder(tree.right_child, value, level + 1, path)


if __name__ == "__main__":
    a = BinaryTree(1)
    a.insertLeft(3)
    a.insertRight(2)
    a.left_child.insertLeft(-2)
    a.left_child.insertRight(-3)
    a.right_child.insertLeft(-1)
    a.right_child.insertRight(-2)
    path_finder(a, 1)

