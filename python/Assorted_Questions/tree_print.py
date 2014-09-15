class Tree(object):
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children

class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def eq(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.head.nextNode = self.tail
            self.tail = self.head
        else:
            self.tail.nextNode = new_node
            self.tail = new_node
        self.size += 1

    def dq(self):
        assert self.size > 0, "Queue is empty"
        value = self.head.value
        self.head = self.head.nextNode
        self.size -= 1
        return value

class Node(object):
    def __init__(self, value=None, nextNode=None):
        self.value = value
        self.nextNode = nextNode
    
    def __repr__(self):
        return self.value

def level_by_level(tree):
    """
    Print binary tree level by level using BFS and a Queue.
    Returns a dictionary that contains {level: [values]}
    """
    queue, table = Queue(), {}
    current = 0
    queue.eq((current, tree))
    while queue.size > 0:
        current += 1
        current_level, current_tree = queue.dq()
        if current_tree.children:
            for child in current_tree.children:
                queue.eq((current, child))
        if current_level in table:
            table[current_level] += [current_tree.value]
        else:
            table[current_level] = [current_tree.value]
    return table

if __name__ == "__main__":
    a = Tree(value=5, \
        children=[Tree(value=6, children=[Tree(value=8)]), Tree(value=7)])
    levels = level_by_level(a)
    for level in sorted(d, levels.keys()):
        print "Level {0} -> {1}".format(level, levels[level])
