def merge(left, right):
    """ Merge two arrays."""
    result = []
    left_index, right_index = 0, 0
    # Hold two separate index pointers to iterate through the two arrays.
    # Iteratively add the lesser element to our results array until either
    # pointer reaches the end of its respective array.
    while left_index < len(left) and right_index < len(right):
        left_value, right_value = left[left_index], right[right_index]
        if left_value <= right_value:
            result.append(left_value)
            left_index += 1
        else:
            result.append(right_value)
            right_index += 1
    # Add remaining elements to the results array.
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


def merge_sort(items):
    """ Recursively divide an array until it consists of single element
    arrays, then merge pairs of arrays together until the entire list of
    items is completely rebuilt. 

    - Runs in O(NlogN) worst-case time
    - Requires 2N space (additional array to merge to/from)
    - Best used on large sets of data, guaranteed NlogN runtime
    - Easily run in parallel
    - More efficient than quicksort for linked lists
    - More efficient than quicksort when dataset is too large for RAM
        - quicksort requires many random seeks, mergesort reads sequentially
    """
    if len(items) <= 1: # Base case
        return items

    midpoint = len(items) / 2
    left = items[0:midpoint]
    right = items[midpoint:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))


def test_merge():
    merged = merge([1, 4, 5], [2, 3, 7, 9])
    assert merged == [1, 2, 3, 4, 5, 7, 9]


def test_merge_sort():
    unsorted = [4, 1, 2, 8, 9, 3]
    result = merge_sort(unsorted)
    assert result == [1, 2, 3, 4, 8, 9]
