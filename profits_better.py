#Q given a list of daily closing price of stock
# _list = [3, 4, 3, 2, 7, 3, 4]
_list = [7, 4, 3, 2, 3, 3, 4] 

def prof_better(array):
    minimum_val = array[0]
    profit = 0
    for i in range(len(array)):
        profit = max(profit, array[i] - minimum_val)
        if array[i] < minimum_val:
            minimum_val = array[i]
    return profit

print(prof_better(_list))