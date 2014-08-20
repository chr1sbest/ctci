def string_is_digit(string):
    """
    Determine if a string is a valid number/float.

    -Can only have one period
    -Can start with +/-
    """
    valids = set([46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57])
    plus_minus = set([43, 45])
    characters = list(string)

    #First character can be number or +/-
    if ord(characters[0]) not in valids.union(plus_minus):
        return False
    
    #Iterate to check all other characters
    for character in string[1:]:
        value = ord(character)
        if value not in valids:
            return False
        elif value == 46:       # 46 = '.'
            valids.remove(46)   # Only one period allowed
    return True



if __name__ == "__main__":
    print string_is_digit('100.124')
    print string_is_digit('100.12.13') 
