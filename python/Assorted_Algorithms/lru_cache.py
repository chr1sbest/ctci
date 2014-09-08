class Node(object):
    """
    Doubly-linked list.
    """
    def __init__(self, value=None, key=None,\
                 nextNode=None, prevNode=None):
        self.value = value
        self.key = key
        self.nextNode = nextNode
        self.prevNode = prevNode

    def __iter__(self):
        node = self
        while node is not None:
            yield str(node)
            node = node.nextNode
    
    def __str__(self):
        return "Key: {0}, Val: {1}".format(self.key, self.value)


class LRU_Cache(object):
    """
    Least-recently used cache. 
    
    Insertion O(1)
    Search O(1)
    Delete O(1)
    """
    def __init__(self, maxSize=5):
        assert maxSize > 1, "Cache size must be larger than 1"
        self.head = Node()
        self.tail = self.head
        self.table = dict()
        self.size = 0
        self.maxSize = maxSize

    def insert(self, key, value):
        if key in self.table:
            # Key already exists in cache.
            self.table[key].value = value
        else:
            # Add new node to hashtable and linked list.
            newNode = Node(key=key, value=value)
            self.table[key] = newNode
            self.size += 1
        self.move_to_front(self.table[key])
        if self.size >= self.maxSize: self.remove_oldest()

    def remove_oldest(self):
        currentNode = self.tail
        self.tail = self.tail.prevNode
        self.tail.nextNode = None
        del self.table[self.tail.key]

    def move_to_front(self, node):
        """
        Move node in linked list to the head. 

        A <-> B <-> C <-> D
          move_to_front(C)
        C <-> A <-> B <-> D
        """
        if node.prevNode:
            node.prevNode.nextNode = node.nextNode
        if node.nextNode:
            node.nextNode.prevNode = node.prevNode
        node.nextNode, node.prevNode = self.head, None
        self.head.prevNode = node
        self.head = node

    def search(self, key):
        if key in self.table:
            node = self.table[key]
            self.move_to_front(node)
            return node.value
        else:
            return False

    def __str__(self):
        values = [str(node) for node in self.head]
        return "\n".join(values)

if __name__ == "__main__":
    cache = LRU_Cache(maxSize=3)
    print "Initializing cache size 3 of [A:1, B:2, C:3]"
    cache.insert('A', 1)
    cache.insert('B', 2)
    cache.insert('C', 3)
    print cache, "\n\nAdding D"
    cache.insert('D', 4)
    print cache, "\n\nAdding E"
    cache.insert('E', 5)
    print cache, "\n\nSearching for D"
    cache.search('D')
    print cache, "\n\nAdding F"
    cache.insert('F', 6)
    print cache, "\n\nAdding G"
    cache.insert('G', 7)
    print cache
