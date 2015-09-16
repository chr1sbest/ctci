def is_permutation(string_1, string_2):
    """ Determine if one string is a permutation of another.
    Time: O(n*logn) -> O(1) BEST CASE
    Space: O(n)
    """
    # Try fastest checks first
    # O(1)
    if len(string_1) != len(string_2):
        return False
    # O(n+m)
    if sum(bytearray(string_1)) != sum(bytearray(string_2)):
        return False

    # Compare sorted chars as final resort, O(n*logn)
    sorted1, sorted2, = sorted(string_1), sorted(string_2)
    for index, char in enumerate(sorted1):
        if char != sorted2[index]:
            return False
    return True 


def test_is_perm():
    assert is_permutation('hi', 'ih') == True
    assert is_permutation('hi', 'hello') == False
