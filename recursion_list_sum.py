def rec_list_sum(_list):
    """Recursion of nested list sum
    Test Data: [1, 2, [3,4], [5,6]]
    Expected Result: 21"""
    total = 0
    for item in _list:
        if isinstance(item, list):
            total + rec_list_sum(item)
        else:
            total + item
    return total
array = [1,2,[3,4],[5,6]]
print(rec_list_sum(array))
