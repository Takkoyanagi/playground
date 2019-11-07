_list = [3, 4, 3, 2, 7, 3, 4]
# _list = [7, 4, 3, 2, 3, 3, 4] 

def max_prof(array):
    """input an array to determine max & sum
    profit by buying low and selling high"""
    
    #edge cases
    if len(array) < 1:
        return 0
    
    # pointers
    low = array[0]
    high = array[0]
    profits = []
    
    # iterate through list and set pointers
    for i in array:
        # if item is less than the high pointer,
        # sell and reinitiate pointers
        if i < high:
            profits.append(high-low)
            low = i
            high = i
        # if item is higher, then new high
        elif i >= high:
            high = i
    # if we have any left over
    if high > low:
        profits.append(high-low)
    print(f"Max profit: {max(profits)} and  Total profit {sum(profits)}")

max_prof(_list)