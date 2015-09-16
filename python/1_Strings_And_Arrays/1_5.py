def compressor(word):
    """ Return a compressed version of string if shorter, else return string.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    new_word = ''
    current_letter, current_count = word[0], 0
    for character in word:
        if character == current_letter:
            current_count += 1
        else:
            compressed = '{}{}'.format(current_letter, current_count)
            new_word += compressed
            current_count = 1
            current_letter = character

    if current_count > 1:
        compressed = '{}{}'.format(current_letter, current_count)
        new_word += compressed
    return new_word if len(new_word) < len(word) else word


def test_compressor():
    assert compressor('aaaabbbcccdddddaaa') == 'a4b3c3d5a3'
    assert compressor('chriss') == 'chriss'
    assert compressor('zzzzzzzz') == 'z8'
