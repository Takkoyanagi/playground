def add_nums(num1, num2):
    """add two numbers without
    addition operators"""
    while num2 != 0:
        #bitwise and for two numbers
        carry = num1 & num2
        # store new bitwise or for num1
        num1 = num1 ^ num2
        # bitwise shift carry by 1
        num2 = carry << 1
    return num1

print(add_nums(5,7))