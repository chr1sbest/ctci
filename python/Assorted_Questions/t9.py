class T9(object):
    _letter_map = {
        'a': '1', 'b': '1', 'c': '1',
        'd': '2', 'e': '2', 'f': '2',
        'g': '3', 'h': '3', 'i': '3',
        'j': '4', 'k': '4', 'l': '4',
        'm': '5', 'n': '5', 'o': '5',
        'p': '6', 'q': '6', 's': '6',
        't': '7', 'u': '7', 'v': '7',
        'w': '8', 'x': '8', 'y': '8', 'z': '8'
    }
    def __init__(self, value=None):
        self.value = value
        self.children = {str(x): None for x in range(9)}
        self.words = []

    def insert(self, full_word, partial_word=None):
        """
        Recursively traverse down trie until final letter.
        Add full word to list of words for the final node.
        """
        partial_word = partial_word or full_word
        if len(partial_word) == 1:
            self.words.append(full_word)
        else:
            current = self._letter_map[partial_word[0]]
            if self.children[current] == None:
                self.children[current] = T9(current)
            self.children[current].insert(full_word, partial_word[1:])

    def search(self, partial_num):
        """
        Given a string of numbers "134512", traverse down the trie and 
        return a list of words that correspond to the T9 interpretation.
        """
        if len(partial_num) == 1:
            return self.words
        else:
            current, new_part = partial_num[0], partial_num[1:]
            return self.children[current].search(new_part)


if __name__ == "__main__":
    t9 = T9()
    t9.insert('can')
    t9.insert('cam')
    t9.insert('bam')
    print t9.search('115')
