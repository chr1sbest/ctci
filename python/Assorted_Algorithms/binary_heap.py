class BinHeap(object):
    def __init__(self):
        self.heaplist = [0]
        self.size = 0

    def percolate_up(self, i):
        """Recursively switch the parent node with current if the
        current is smaller."""
        while i // 2 > 0:
            upval = i // 2
            if self.heaplist[i] < self.heaplist[upval]:
                tmp = self.heaplist[upval]
                self.heaplist[upval] = self.heaplist[i]
                self.heaplist[i] = tmp
            i = upval

    def insert(self, k):
        """Insert new value at the end of the binary heap and recursively
        percolate it upwards until it is in the appropriate spot."""
        self.heaplist.append(k)
        self.size += 1
        self.percolate_up(self.size)

    def percolate_down(self, i):
        """Recursively switch the parent node with current if the 
        current is bigger."""
        while i * 2 <= self.size:
            downval = self.min_child(i)
            if self.heaplist[i] > self.heaplist[downval]:
                tmp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[downval]
                self.heaplist[downval] = tmp
            i = downval

    def min_child(self, i):
        """Return the child with a lower value. If there is only one child,
        return that child."""
        try:
            child1, child2 = self.heaplist[i * 2], self.heaplist[i * 2 + 1]
            return i * 2 if child1 > child2 else i * 2 + 1
        except IndexError:
            return i * 2

    def pop_minimum(self):
        """Dequeue the minimum value on the priority queue."""
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist[-1]
        self.size -= 1
        self.heaplist.pop()
        self.percolate_down(1)
        return retval

    def build_heap(self, array):
        """Build a heap quickly in O(n)."""
        i = len(array) // 2
        self.size = len(array)
        self.heaplist = [0] + array[:]
        while i > 0:
            self.perc_down(i)
            i -= 1
