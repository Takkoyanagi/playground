def sp_count(n):
    """ 
    Leetcode-36
    The count-and-say sequence is the sequence of integers with the first five terms as following:

    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221

    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.

    Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
    """
    # base case
    if n == 1:
        return "1"
    else:
        # initialize variables
        nums = []
        count = 0
        # recursively get previous number
        prev = sp_count(n-1)
        # pointer variable
        temp = prev[0]
        for i in range(len(prev)):
            # if the numbers are the same
            # we increase count
            if prev[i] == temp:
                count += 1
            else:
                # otherwise, append to list
                nums.append(str(count))
                nums.append(str(temp))
                # move pointer
                temp = prev[i]
                # reset count to 1
                count = 1
        nums.append(str(count))
        nums.append(str(temp))
        return ''.join(nums)


print(sp_count(4))
