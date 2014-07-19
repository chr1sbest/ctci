def bucket_sort(array, bucket_range=10):
    """
    Time complexity: O(n+k)
    """
    
    buckets = [[] for x in range(bucket_range)]
    for index, val in enumerate(array):
        buckets[val].append(val)
    return [value for sublist in buckets for value in sublist]

if __name__ == "__main__":
    a = [1, 5, 4, 2, 7, 6, 1, 1, 2]
    b = bucket_sort(a)
    print a, b
