def shellSort(array):
    """ insertion sort subsets"""
    subset_val = len(array)//2
    while subset_val > 0:
        for i in range(subset_val):
            gap_insertion_sort(array, i, subset_val)
        subset_val = subset_val//2
    return array


def gap_insertion_sort(array, start, gap):
    for i in range(start+gap, len(array), gap):
        current_val = array[i]
        position = i

        while position >= gap and array[position-gap] > current_val:
            array[position] = array[position-gap]
            position -= gap
        array[position] = current_val
    return array


array = [1, 777, 8, 9, 5, 3, 222, 5, 66, 9]
print(shellSort(array))
