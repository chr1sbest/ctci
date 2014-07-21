def three_sum(target, array):
    """
    Given an array of integers, return all three-integer combinations that total
    up to the target value.

    Time complexity: O(n^2)
    """
    array = sorted(array)
    solutions = []
    for index, val in enumerate(array[:-2]):
        begin = index + 1
        end = len(array) - 1
        while begin < end:
            total = val + array[begin] + array[end]
            if total == target:
                solutions.append([val, array[begin], array[end]])
            if total > target:
                end -= 1
            else:
                begin += 1
    return solutions

if __name__ == "__main__":
    print three_sum(3, [-1, -2, -3, 0, 1, 2, 3, 4, -5])
