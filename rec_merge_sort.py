#! python3
def rec_mergeSort(array):
    """ Perform merge sort by recursively splitting array into
    halves until all the values are separated
    then do a piece wise comparason to fill the array in order
    """
    # check if array is none
    if len(array) > 1:
        # find mid index of list
        mid = len(array) // 2
        # split the array in half
        l = array[:mid]
        r = array[mid:]
        # recursively keep splitting
        rec_mergeSort(l)
        rec_mergeSort(r)

        # initialize variables
        i = j = k = int(0)

        # while either l or r exists
        while i < len(l) and j < len(r):
            # compare values in l and r then fill lower value
            if int(l[i]) < int(r[j]):
                array[k] = l[i]
                i += 1 # scan through list l
            else:
                array[k] = r[j]
                j += 1 # scan through list r
            k += 1 # scan through array
        
        # only list l remains
        while i < len(l):
            array[k] = l[i]
            i += 1
            k += 1
        # only list r remains
        while j < len(r):
            array[k] = r[j]
            j += 1
            k += 1
    return array

array = [-3,0,1,-3,1,1,1,-3,10,0]
print(rec_mergeSort(array))