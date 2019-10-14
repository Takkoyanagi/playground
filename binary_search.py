def binary_search(item_list, item):
    """"perform binary search
    list = item_list
    item = value in list """
    #initialize index variable
    item_list.sort()
    first = 0
    last = len(item_list) - 1
    found = False
    # edge case check if all items in list are num
    if all(isinstance(n,(int,float)) for n in item_list):
        while (first <= last and not found):
            #define midpoint
            mid = (first + last) // 2
            if item_list[mid] == item:
                found = True
            else:
                if item < item_list[mid]:
                    last = mid - 1 
                else:
                    first = mid + 1
        return found
    else:
        print('items needs to be integers')
    

print(binary_search([-1,-3.5,-5,15,29,1], -3.5))