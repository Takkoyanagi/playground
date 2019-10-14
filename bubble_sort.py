def bubbleSort(array):
    """Sorts array by continually swapping items if
    item is in wrong order"""
    # ensures all values in the array are numbers
    if all(isinstance(x, (int,float)) for x in array):
        n = len(array)
        # need number of items in array to traverse
        for i in range(n):  
            for j in range(n-i-1): # the last value will be in order
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j] #swap
        return array
    else:
        print('values in array needs to be a number')

array = [ 1,6,3,8,9,0,"1",-5]
print(bubbleSort(array))


