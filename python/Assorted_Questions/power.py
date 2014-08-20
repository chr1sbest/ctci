def naive_pow(base, exp):
    """
    Calculate base^exp using naive iteration.
    Time complexity: O(n)
    """
    result = 1
    for value in xrange(0, exp):
        result = result * base
    return result

def pow(base, exp):
    """ 
    Calculate base^exp by using "exponentiation by squaring".
    Time complexity: O(logn)
    """
    if exp == 1:
        return base
    if exp % 2 == 0:
        return pow(base * base, exp / 2)
    else:
        return base * pow(base * base, (exp - 1) / 2)

if __name__ == "__main__":
    print naive_pow(2, 3)
    print pow(2, 3)
