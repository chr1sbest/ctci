def shell_sort(array):
    skip = len(array) // 2
    while skip > 0:
        for index, val in enumerate(array):
            while index >= skip and array[index - skip] > val:
                array[index] = array[index - skip]
                index -= skip
            array[index] = val
        skip = skip // 2

if __name__ == "__main__":
    a = [3, 22, 123, 152, 43, 23]
    print a
    shell_sort(a)
    print a
