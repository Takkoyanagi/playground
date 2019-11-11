def mergeSort(array):
    """sort recursively using divide and
    conquer"""
    print('splitting', array)
    if len(array) > 1:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]
        mergeSort(left)
        mergeSort(right)
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    print('Merging', array)
    return array


array = [1, 2, 3, 44, 555, 222, 333, 444, 909]
print(mergeSort(array))
