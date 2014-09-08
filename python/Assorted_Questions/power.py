def naive_pow(base, exp):
    """
    Calculate base^exp using naive iteration.
    Time complexity: O(n)
    """
    result = 1
    for value in xrange(0, exp):
        result = result * base
    return result

def pow(base, exp, tmp=1):
    """ 
    Calculate base^exp by using "exponentiation by squaring".
    Time complexity: O(logn)
    """
    if exp == 1:
        return base * tmp
    if exp % 2 == 0:
        return pow(base * base, exp / 2, tmp)
    else:
        return pow(base * base, (exp - 1) / 2, tmp * base)

if __name__ == "__main__":
    print naive_pow(2, 3)
    print pow(2, 7)
