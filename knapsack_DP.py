def knapsack_bottUp(W, wt, val, n):
    """Bottom up dynamic programming to find
    the optimal weight/value to add to the knapsack
    W = max weight knapsack can hold
    wt = array of weights
    val = array of values associated to weights
    n = length of arrays
    """
    # create a matrix of n+1 by W+1 of 0 
    K = [[0 for x in range(W+1)] for x in range(n+1)]
    
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][W]

# Driver program to test above function 
val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print(knapsack_bottUp(W, wt, val, n)) 