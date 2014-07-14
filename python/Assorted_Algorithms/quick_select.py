def quick_select(array, k):
    """
    Find kth element in an unsorted array without sorting.
    Recursively partition the array around a pivot.

    Time complexity: O(n) average, O(n^2) worst
    """
    pivot = len(array) // 2
    lesser, pivots, greater = partition(array, array[pivot])
    if k in range(len(lesser), len(lesser) + len(pivots)):
        return array[pivot]
    elif k < len(lesser):
        return quick_select(lesser, k)
    else:
        k = k - (len(lesser) + len(pivots))
        return quick_select(greater, k)

def partition(array, pivot_val):
    """
    Partitions around a pivot element and returns an array
    for each lesser, greater, and pivots.

    'Pivots' array is to handle duplicate pivot values.
    """
    lesser, pivots, greater = [], [pivot_val], []
    for element in array:
        if element < pivot_val:
            lesser.append(element)
        elif element > pivot_val:
            greater.append(element)
        else:
            pivots.append(element)
    return lesser, pivots, greater

if __name__ == "__main__":
    a = [1, 4, 8, 3, 3, 0, 4, 5, 8]
    b = sorted(a)
    k = 5
    print "Index[{0}] of sorted array is {1}".format(k, b[k])
    print "Quick select {0}th element of array is {1}".format(k, quick_select(a, k))
