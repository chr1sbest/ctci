def reverse_null_terminated_string(input_string):
    """Reverse a null-terminated string."""
    assert input_string[-1] in [None, '*']
    # Slice the string from 0->null char, reverse this slice
    # and then add the null char to the end.
    return input_string[:-1][::-1] + input_string[-1:]


def test_reverse():
    chris = reverse_null_terminated_string('chris*')
    assert chris == 'sirhc*'
    what = reverse_null_terminated_string(['w','h','a','t','*'])
    assert what == ['t', 'a', 'h', 'w', '*']
