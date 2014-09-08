def find_value(value, matrix):
    """
    Determine if value is in a matrix using Down-Left algorithm.

    Time Complexity = O(N + M) -> in an NxM matrix
    """
    dimension1, dimension2 = len(matrix), len(matrix[0])
    index1, index2 = 0, dimension2 - 1
    while index1 < dimension1 and index2 >= 0:
        current = matrix[index1][index2]
        if current == value:
            return True
        elif current < value:
            index1 += 1
        else:
            index2 -= 1
    return False





if __name__ == "__main__":
    matrix = [[x + y * 10 for x in xrange(10)] for y in xrange(10)]
    print find_value(40, matrix)
