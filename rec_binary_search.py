def rec_binary_search(array, l, u, num):
    """recursively performs binary search for a given
    array.
    l = lower index set to zero
    u = upper index set to zero
    num = target value
    """
    if all(isinstance(x, (int, float)) for x in array):
        if l < u:
        #initialize the upper/lower index
            mid = (l+u)//2 #find midway point
            if array[mid] == num:
                return True
            elif num < array[mid]:
                return rec_binary_search(array, l, mid-1, num)
            else: 
                return rec_binary_search(array, mid+1, u, num)
        else:
            return False
    else:
        print('all values in array must be numbers')
array = [1,23,4,5,6,6,"7",6]
print(rec_binary_search(array,0, len(array)-1, 6))