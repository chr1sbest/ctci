def unique(input_string, total_letters=128):
    """ Determine if all characters in a string are unique.
    Keep a hashtable to record whether a character has been seen while
    iterating over all of the characters in the input string.

    Time: O(n)
    Space: O(n)
    """
    # Return in O(1) if impossible for all unique
    if len(input_string) > total_letters:
        return False

    # Initialize boolean hashtable of size = totalLetters
    letters = {}
    for letter in input_string:
        if letter in letters:
            return False
        letters[letter] = True
    return True

def unique_alternate(input_string):
    """ Determine if all characters in a string are unique. Sort the string
    and then iterate over each character, comparing each character to the
    previous character.

    Time: O(n*log(n))
    Space: O(1)
    """
    sorted_string = ''.join(sorted(input_string))
    last_character = None
    for index, letter in enumerate(sorted_string):
        if letter == last_character:
            return False
        last_character = letter
    return True

def test_unique():
    assert unique('hello_friend') == False
    assert unique_alternate('hello_friend') == False
    assert unique('waldo') == True
    assert unique_alternate('waldo') == True
