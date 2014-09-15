def isomorphic(word1, word2):
    """
    Determine if characters in one string can be mapped to characters
    in a second string. 
    app -> boo = True {a:b, p:o}
    foo -> bar = False {f:b, o:a, o:r}
    """
    letter_map = {}
    for index, letter in enumerate(word1):
        if letter in letter_map and letter_map[letter] != word2[index]:
            return False
        letter_map[letter] =  word2[index]
    return True


if __name__ == "__main__":
    word1, word2 = 'app', 'boo'
    print "{0} -> {1} is {2}".format(\
        word1, word2, isomorphic(word1, word2))
    word3, word4 = 'turtle', 'tletur'
    print "{0} -> {1} is {2}".format(\
        word3, word4, isomorphic(word3, word4))
    word5, word6 = 'foo', 'bar'
    print "{0} -> {1} is {2}".format(\
        word5, word6, isomorphic(word5, word6))
