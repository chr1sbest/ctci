def mssl(array):
    """
    Find the indexes of the largest successive sum in an array.

    Time Complexity: O(n)
    """
    best, current = 0, 0
    start_index, end_index, current_index = 0, 0 ,0
    for index, value in enumerate(array):
        if current + value > 0:
            current += value
        else:
            current, current_index = 0, index + 1
        if current > best:
            start_index, end_index = current_index, index + 1
            best = current
    # One extra step to handle array of all negative numbers.
    mssl = array[start_index:end_index]
    return mssl if mssl != [] else [max(array)]

        

if __name__ == "__main__":
    print mssl([4, -2, -8, 5, -2, 7, 7, 2, -6, 5])
    print mssl([-312, -123, -32, -45, -1])
