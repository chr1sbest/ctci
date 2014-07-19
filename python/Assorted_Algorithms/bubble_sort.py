def bubble_sort(array):
    """
    Time Complexity: O(n^2)
    """
    finished = False
    while not finished:
        finished = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                finished = False
    return array


if __name__ == "__main__":
    a = [1,5,4,2,7,6]
    print a, bubble_sort(a)



