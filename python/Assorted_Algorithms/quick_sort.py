def quick_sort(array):
    """
    Time compelxity: O(nlogn) average
                     O(n^2) worst case
    -In place
    -Not Stable
    -Divide and Conquer
    """
    if len(array) < 2:
        return array
    else:
        pivot = array[0]    # can optimize to find better pivot.
        less = filter(lambda x: x < pivot, array)
        equal = filter(lambda x: x == pivot, array)
        greater = filter(lambda x: x > pivot, array)
        return quick_sort(less) + equal + quick_sort(greater)

if __name__ == "__main__":
    a = [1, 5, 23, 13, 51, 34]
    b = quick_sort(a)
    print a, b

