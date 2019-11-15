A = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]


def flip_invert_image(array):
    """flips and inverts (1 -> 0 and 0 -> 1) matrix"""
    return [list((map(lambda x: 1-x, a[::-1]))) for a in A]


print(flip_invert_image(A))
