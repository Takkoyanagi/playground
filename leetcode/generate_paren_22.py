# given number n, generate parentheses


def recursive_paren(array, n):
    """recursive helper function to
    parse through previous array to 
    add parentheses
    """
    if n == 1:
        return array
    else:
        output = []
        output.append(array[0]+'()')
        for item in array:
            for index, character in enumerate(item):
                if character == '(':
                    output.append(item[0:index+1]+'()'+item[index+1:])
    return recursive_paren(output, n-1)


def gen_paren(n):
    """ Generate all possible combinations
    of parentheses from number, n
    """
    # edge case
    if n == 0:
        return []
    array = ['()']
    return recursive_paren(array, n)


print(gen_paren(10))
