def is_rotation(string_1, string_2):
    """ Determine if string_1 is a substring of string_2 by doubling string_2.
    If s1 = xy, and s2 = yx, s1(xy) will always be a substring of s2s2(yxyx).
    """
    return string_1 in string_2 + string_2

def test_rotation():
    assert is_rotation('waterbottle', 'terbottlewa') == True
    assert is_rotation('chris', 'sirhc') == False
