def fib_list(n):
    """computationally more efficient fib using lists"""
    fib = [0,1]
    for i in range(2,n+1):
        fib.append(fib[i-2] + fib[i-1])
    return fib[-1]

print(fib_list(530))