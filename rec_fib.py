def rec_fib(n):
    """returns the nth fibonacci number recursively"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rec_fib(n-1) + rec_fib(n-2)

print(rec_fib(5))