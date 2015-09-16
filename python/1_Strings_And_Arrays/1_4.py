def string_filler(input_string):
    """Returns a new string with spaces replaced by %20"""
    return ''.join(input_string.replace(' ', '%20'))


def better_string_filler(input_string):
    """ Builds an empty string of appropriate size then sets
    appropriate characters at appropriate index.
    Time: O(n)
    Space O(n)
    """
    # Calculate the array length required for a string that will
    # replace spaces with %20.
    space_length = len(filter(lambda x: x == " ", input_string))
    true_length = len(input_string) + (space_length * 2)
    new_string = [None] * true_length

    leader = 0 
    for index, char in enumerate(input_string):
        index_plus = index + leader
        if char == " ":
            new_string[index_plus:index_plus + 3] = list("%20")
            leader += 2
        else:
            new_string[index_plus] = char
    return ''.join(new_string)
        

def test_string_filler():
    expected = 'hello%20my%20name%20is%20chris'
    assert string_filler('hello my name is chris') == expected
    assert better_string_filler('hello my name is chris') == expected
