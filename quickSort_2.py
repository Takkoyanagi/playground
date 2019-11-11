def quickSort(array):
    """ sort array by dividing and conquering
    inplace"""
    quickSortSplitter(array, 0, len(array)-1)
    return array


def quickSortSplitter(array, start, end):
    """ splits the array into subarrays"""
    if start < end:

        split_point = partition(array, start, end)

        quickSortSplitter(array, start, split_point-1)
        quickSortSplitter(array, split_point+1, end)


def partition(array, start, end):
    """ sets up markers for pivot point, left marker
    and right marker then iteratively swap into place
    as the markers converge"""
    # initialize variables
    piv = array[start]
    left = start+1
    right = end
    done = False  # create switch

    while not done:
        # iterate pointer through without swap if item is
        # less than pivot point
        while (left <= right) and (array[left] <= piv):
            left += 1
        # iterate pointer through without swap if item is
        # greater than pivot point
        while (array[right] >= piv) and (right >= left):
            right -= 1
        if right < left:
            done = True  # switch to break loop
        # otherwise, swap items
        else:
            temp = array[left]
            array[left] = array[right]
            array[right] = temp
    temp = array[start]
    array[start] = array[right]
    array[right] = temp

    return right


array = [33, 1, 344, 2, 33, 5, 3, 666, 7, 0]

print(quickSort(array))
