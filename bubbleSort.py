arr = [5,2,5,4,7]

# for i in range(len(arr)-1, 0, -1):
#     for j in range(i):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]

def bubbleSort2(array):
    """Bubble sort with while loop
    to stop if array is sorted"""
    #inititate variables
    swapped = True
    pass_num = len(array) - 1

    # while we are still swapping and pass
    # number is not 0 
    while swapped and pass_num > 0:
        swapped = False #switch off swapped
        for i in range(pass_num): # shrinking range
            if array[i] > array[i+1]: # if out of order, swap
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True # flip swapped on
        pass_num -= 1 #decrease window of search
    return array
print(bubbleSort2(arr))