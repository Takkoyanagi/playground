"""Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. 
No two values have the same number of occurrences."""
array = [1,1,2,1,2,3]

# arr = [-3,0,1,-3,1,1,1,-3,10,0]
# arr = [1,2]

# create a dictionary of each item in list, then count each item
dic_array = {x:array.count(x) for x in array}

# if the length of list of dictionary values are equal 
# to the length of the set, then argument holds true
len(list(dic_array.values())) == len(set(list(dic_array.values())))