def add_nums(num1, num2):
    """add two numbers without
    addition operators using recursion"""
    if num2 == 0:
        return num1
    else:
        return add_nums(num1^num2, (num1&num2)<<1) 
print(add_nums(5,7))