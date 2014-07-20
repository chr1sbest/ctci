def k_way_merge(list_dict):
    """
    Place smallest element of each linked_list (for k arrays) onto a MinHeap.
    Pop the smallest item on the heap, add it to the new array, and then add the
    next smallest item from the array that the smallest item belonged to.

    list_dict = {
        1: Node(3, Node(5, Node(7, None))),
        2: Node(1, Node(3, Node(6, None))),
        3: Node(2, Node(8, Node(9, None))),
        4: Node(5, Node(6, Node(8, None)))
    }
    
    Time Complexity: O(nlogk)
    Space Complexity: O(k)
    """
    result = []
    heap = MinHeap()            
    # Build initial heap using min from each linked list in list_dict
    for key in list_dict.keys():
        value = list_dict[key].pop_front()
        heap.add((value, key))  # Keep track of which linked list (key)

    while heap.peek():          # Return if heap is empty        
        value, key = heap.pop() # Pull out min value from heap
        result.append(value)
        try:                    # Refill heap with new value
            new_val = list_dict[key].pop_front()
            heap.add((new_val, key))       
        except:
            print 'Array {0} finished'.format(key)
            pass
    return result


class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def pop_front(self):
        data = self.data
        self.data = self.next.data
        self.next = self.next.next
        return data

class Heap(object)
    def __init__(self):
        pass
