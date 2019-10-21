def knapsack(value, weights, knapw):
    """Optimize the value inside knapsack while 
    staying under max weight of knapsack
    value = array of values
    weights = array of weights associated with value
    knapw = maximum weight knapsack can hold"""
    stuff = {}
    value = sorted(value, reverse=True)
    if isinstance(weights, list):
        weights = sorted(weights, reverse=True)
    

    while isinstance(weights,list) and len(weights) > 0:
        for i in weights:
            if i > knapw:
                knapsack(value, weights.pop(0), knapw)
            elif i < knapw and (sum(stuff.keys()) + i) < knapw:
                stuff[i] = value[weights.index(i)]
                knapsack(value, weights.pop(0), knapw)
            else:
                knapsack(value, weights.pop(0), knapw)
    return sum(stuff.values())



value = [60,100,120]
weights = [10,20,30]
knapw = 50
print(knapsack(value, weights,knapw))

