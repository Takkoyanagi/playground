def _sum(array):
    """ Recursively find the sum of array"""
    count = 0
    while array:
        count += array[-1]
        array.pop()
        print(array)
    return count
array = [1,3,5,7]       
print(_sum(array))