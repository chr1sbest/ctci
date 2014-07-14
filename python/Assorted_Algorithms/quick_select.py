def quick_select(array, k):
    """
    Find kth element in an unsorted array without sorting.
    Partitions around a middle element and then recursively
    checks the appropriate partition for the value.

    Time complexity: O(n)
    """
    pivot = len(array) // 2
    pivot_el = array[pivot]
    lesser, greater, pivots = [], [], [pivot_el]
    for element in array:
        if element < pivot_el:
            lesser.append(element)
        elif element > pivot_el:
            greater.append(element)
        else:
            pivots.append(element)
    if k in range(len(lesser), len(lesser) + len(pivots)):
        return pivot_el
    elif k < len(lesser):
        return quick_select(lesser, k)
    else:
        k = k - (len(lesser) + len(pivots))
        return quick_select(greater, k)

if __name__ == "__main__":
    a = [1, 4, 8, 3, 3, 0, 4, 5, 8]
    b = sorted(a)
    k = 5
    print "Index[{0}] of sorted array is {1}".format(k, b[k])
    print "Quick select {0}th element of array is {1}".format(k, quick_select(a, k))
