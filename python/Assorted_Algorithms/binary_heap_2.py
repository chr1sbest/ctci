from sys import maxint
from unittest import TestCase

class EmptyHeapException(Exception):
    pass

class MinHeap(object):
    """
    Pop minimum - O(1)
    Insert - O(logn)
    """
    def __init__(self):
        self.heap = [0]

    def pop(self):
        """ Swap the first(min) and last elements of the heap, then
        remove the first(min) from the heap and percolate the last element
        of the heap downwards until it is in the right spot."""
        if self.heap == [0]:
            raise EmptyHeapException('Heap is empty.')
        self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
        minimum = self.heap[-1]     # Store min val to return later
        self.heap = self.heap[:-1]  # Remove final element
        self._percolate_down(1)
        return minimum

    def insert(self, value):
        """ Insert a new key into the binary heap in O(logn) worst case."""
        self.heap.append(value)
        index = len(self.heap) - 1
        self._percolate_up(index)

    def _percolate_up(self, index):
        child = self.heap[index]
        parent = self.heap[index / 2]
        if child < parent:
            self._swap(index, index / 2)
            self._percolate_up(index / 2)

    def _percolate_down(self, index):
        """ Recursively swap child with parent if parent is larger than child.
        Otherwise, percolation is complete and the heap is once again complete.
        If there is no child, we will assume an infinitely large number.
        """
        parent = self.heap[index]
        child_2_index, child_1_index = index * 2, index * 2 + 1
        try:
            child_1_value = self.heap[child_1_index]
        except IndexError:
            child_1_value = maxint
        try:
            child_2_value = self.heap[child_2_index]
        except IndexError:
            child_2_value = maxint
        if parent > child_1_value or parent > child_2_value:
            # Swap parent with lesser child and then recursively percolate
            # the new child (previous parent) downwards
            if child_1_value > child_2_value:
                self._swap(child_2_index, index)
                self._percolate_down(child_2_index)
            else:
                self._swap(child_1_index, index)
                self._percolate_down(child_1_index)

    def _swap(self, i1, i2):
        self.heap[i1], self.heap[i2] = self.heap[i2], self.heap[i1]


class MinHeapTest(TestCase):
    def setUp(self):
        self.minheap = MinHeap()

    def test_pop(self):
        """   1           9          4
            4   7  ->   4   7  ->  9   7
          9           1   
        """
        self.assertRaises(EmptyHeapException, self.minheap.pop)
        self.minheap.heap = [0, 1, 4, 7, 9]
        assert self.minheap.pop() == 1
        assert self.minheap.heap == [0, 4, 9, 7] 

    def test_insert(self):
        """   1           1          1
            4   6  ->   4   6 ->   2   6
           9           9 2        9 4
        """
        self.minheap.heap = [0, 1, 4, 6, 9]
        self.minheap.insert(2)
        assert self.minheap.heap == [0, 1, 2, 6, 9, 4]

    def test_percolate_down(self):
        self.minheap.heap = [0, 7, 1, 4, 5, 9, 12]
        self.minheap._percolate_down(1)  # Will percolate 7 downwards
        assert self.minheap.heap == [0, 1, 5, 4, 7, 9, 12]

    def test_swap(self):
        self.minheap.heap = [0, 1, 2]
        self.minheap._swap(0, 2)
        assert self.minheap.heap == [2, 1, 0]
