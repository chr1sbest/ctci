def radix(array, radix=10, sig_dig=1):
    """
    Time complexit O(kn) with k as the difference in significant digits
    between the highest and lowest number.
    """
    finished = False
    while not finished:
        finished = True
        buckets = [list() for x in range(radix)]
        for element in array:
            if element / sig_dig > 0:
                finished = False
            bucket_index = (element / sig_dig) % radix
            buckets[bucket_index].append(element)

        # flatten contents of [buckets] back into array
        array = [val for bucket in buckets for val in bucket]
        sig_dig *= radix
    return array


if __name__ == "__main__":
    a = [1,345,123,235,34,12,52,32]
    b = radix(a)
    print a, b
