def perfect_squares(n):
    """determine how many perfect squares
    adds up to number n"""

    # create a list for dynamic progamming
    dp = [x for x in range(n+1)]

    current = 2

    while current ** 2 <= n:
        for i in range(current**2, n+1):
            dp[i] = min(dp[i], dp[i-current**2]+1)
        current += 1
    return dp[-1]


print(perfect_squares(1))
