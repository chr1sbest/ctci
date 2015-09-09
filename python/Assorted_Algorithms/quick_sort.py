def quick_sort(array, determine_pivot=None):
    """ Recursively sort the array by determining a pivot point and
    splitting elements that are greater / less-than / equal to the pivot.

    - O(nlogn) average, typically outperforms merge sort.
    - O(n^2) worst case. Can avoid this with smarter determine_pivot func.
    - In place
    - Not Stable

    :param determine_pivot: Function that returns a pivot element from array.
    """
    if len(array) < 2:
        return array

    # Determine the pivot to use for sorting this array. Use the
    # determine_pivot function if one is passed in. Otherwise, we will
    # select the first element to use as a pivot by default.
    determine_pivot = determine_pivot or (lambda x: x[0])
    pivot = determine_pivot(array)

    less, equal, greater = partition(array, pivot)
    return quick_sort(less) + equal + quick_sort(greater)


def partition(array, pivot):
    less, equal, greater = [], [], []
    for element in array:
        if element < pivot:
            less.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            greater.append(element)
    return less, equal, greater


def test_quick_sort():
    result = quick_sort([1, 5, 23, 13, 51, 34])
    assert result == [1, 5, 13, 23, 34, 51]


def test_partition():
    array = [1, 10, 3, 8, 5]
    pivot = 5
    (less, equal, greater) = partition(array, pivot)
    assert (less, equal, greater) == ([1, 3], [5], [10, 8])
