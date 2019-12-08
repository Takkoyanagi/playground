# Leetcode 326
def recursive_3(n, memo):
    """recursively determines if n
    is a cleanly divisible by 3
    """
    # Basecase
    if n == 1:
        return True
    elif n in memo:
        return memo[n]
    elif n % 3 == 0:
        memo[n] = n/3
        return recursive_3(n/3, memo)
    else:
        return False


def isPowerOfThree(n):
    memo = {}
    if n == 0:
        return False
    else:
        return recursive_3(n, memo)
