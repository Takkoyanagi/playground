n = 2
m = 3
indices = [[0, 1], [1, 1]]


def num_odd(n, m, indices):
    """returns the number of odds
    after indices flips"""
    # initialize variables
    row, col = [False] * n, [False] * m

    # iterate through indices
    for r, c in indices:
        row[r] ^= True
        col[c] ^= True
    return sum(rows ^ colm for rows in row for colm in col)


print(num_odd(n, m, indices))
