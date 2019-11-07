#Q given a list of daily closing price of stock
# _list = [3, 4, 3, 2, 7, 3, 4]
# _list = [7, 4, 3, 2, 3, 3, 4] 
_list = [] 
#maximum profit that could have been earned given the info provided
def mxprofit(array):
    """Determines the maximum profit that could
    be gained by buying low and selling high"""

    #initialize variables
    minimum_val = 10000
    profit = 0
    # edge cases
    if len(array) <= 1:
        return 0
    # iterate through list and store minimum value
    for i in range(len(array)):
        if array[i] < minimum_val:
            minimum_val = array[i]
        # subtract from minimum value and store profit
        for j in array[i:len(array)]:
            if (j-minimum_val) > profit:
                profit = j - minimum_val
    return profit

print(mxprofit(_list))