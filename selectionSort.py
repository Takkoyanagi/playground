def selectionSort(array):
    """ Sorts an array using
    by finding the max item and
    moving it to the last location
    iteratively"""

    for i in range(len(array), 0, -1):
        # initiate variables
        max_item = 0
        for j in range(i):  # search through shirinking window
            if array[j] > array[max_item]:  # look for max item
                max_item = j
        array[j], array[max_item] = array[max_item], array[j]  # swap

    return array


array = [4, 6, 7, 2, 4, 2, 5, 7, 1, 13]

print(selectionSort(array))
