def bubble_sort_rc(array):
    """perform bubble search recursively"""
    # Check whether all values in list are numbers
    if all(isinstance(x, (int,float)) for x in array):
        for ind, val in enumerate(array):
            try:
                if array[ind+1] < val:
                    array[ind] = array[ind+1]
                    array[ind+1] = val
                    bubble_sort_rc(array)
            except IndexError: 
                pass
        return array
    else:
        print("all values in array needs to be a number")
array = [2,5,3,4,5,7,"8",-1]
print(bubble_sort_rc(array))