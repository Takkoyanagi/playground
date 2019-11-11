def insertionSort(array):
    """ sort an array by inserting items
    where appropriate by iterating through
    an array """

    # iterate through list starting from second
    # value
    for i in range(1, len(array)):
        # initialize variables
        current_val = array[i]
        # check where current value should be
        while i > 0 and array[i-1] > current_val:
            array[i] = array[i-1]  # shift item by one
            i -= 1  # search left
        array[i] = current_val  # insert value into correct place
    return array


array = [2, 5, 7, 88, 4, 2, 1, 3, 33, 6]
print(insertionSort(array))
