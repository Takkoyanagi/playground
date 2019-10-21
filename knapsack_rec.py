def knapsack_rec(W, val, weight, n):
    """recursive knapsac problem where
    W = max weight knapsack can hold
    val = array of values
    weight = array of weights associated with values
    n = length of the arrays
    """
    # Base case
    if n == 0 or W == 0:
        return 0
    # if weight of item is more than max wt of knapsack
    if weight[n-1] > W:
        return knapsack_rec(W, val, weight, n-1)
    
    # if weight can be added to the knapsack
    else:
        return max(val[n-1] + knapsack_rec(W-weight[n-1], val, weight, n-1), 
                    knapsack_rec(W, val, weight, n-1))

# To test above function 
val = [60, 100, 120] 
weight = [10, 20, 30] 
W = 50
n = len(val) 
print(knapsack_rec(W, val, weight, n))