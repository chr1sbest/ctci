def rotator(matrix):
    """ Returns the original matrix rotated by 90 degrees."""
    return zip(*matrix[::-1])

def test_rotator():
    matrix =   [(1, 2, 3),
                (4, 5, 6),
                (7, 8, 9)]

    expected = [(7, 4, 1),
                (8, 5, 2),
                (9, 6, 3)]

    assert rotator(matrix) == expected
