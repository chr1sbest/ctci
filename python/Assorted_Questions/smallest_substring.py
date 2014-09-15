from copy import deepcopy

def smallest_substring(string, chars):
    """
    Given set of characters and a string, find smallest 
    substring which contains all characters.

    'that is a brown cow' 'abc' -> 'a brown c'
    """
    # Initialize variables and data structures
    best = string
    start, end = 0, 0 
    char_hist, window_hist = Histogram(), Histogram()
    for char in chars:
        char_hist.add(char)

    for index, letter in enumerate(string):
        if letter in char_hist.table:
            window_hist.add(letter)
            char_hist.sub(letter)
            if char_hist.total == 0:
                end = index + 1
                best = string[:end]
                break

    for letter in best:
        if letter in window_hist.table:
            if window_hist.table[letter] == 0:
                break
            else:
                window_hist.sub(letter)
                start += 1
    best = best[start:]
    return best


class Histogram(object):
    def __init__(self):
        self.table = {}
        self.total = 0

    def add(self, key):
        if key in self.table:
            self.table[key] += 1
        else:
            self.table[key] = 1
        self.total += 1
        return self.table[key]

    def sub(self, key):
        assert key in self.table, "Key not in table"
        if self.table[key] == 0:
            return False
        self.table[key] -= 1
        self.total -= 1
        return True


if __name__ == "__main__":
    s1, c1 = 'that is a brown cow', 'abc'
    s2, c2 = 'acbbaca', 'abca'
    print s1, c1, smallest_substring(s1, c1)
    print s2, c2, smallest_substring(s2, c2)

