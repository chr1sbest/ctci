def successive_product(array):
    """
    Find the maximum successive product in an array.
    """
    best, temp = 1, 1
    for value in array:
        if value >= 1:
            temp *= value
            if temp > best:
                best = temp
    return best if temp < 0 else temp

if __name__ == "__main__":
    a = [-2, -3, 10, -4, -2]
    print successive_product(a)
