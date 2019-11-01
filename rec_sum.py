def _sum(array):
    """ Recursively find the sum of array"""
    if len(array) == 1:
        return array[0]
    else:
        return array[0] + _sum(array[1:])
        
array = [1,3,5,7]       
print(_sum(array))