def fib_mem(n, computed={0:0,1:1}):
    """find fibonacci number using memoization"""
    if n not in computed:
        computed[n] = fib_mem(n-1, computed) + fib_mem (n-2, computed)
    return computed[n]

print(fib_mem(35))