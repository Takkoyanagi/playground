def recursive_helper(string, count, L):
    # base case
    if len(string) == 0:
        return True
    elif count > 1 or L < 2:
        return False
    else:
        if string[0] == 'A':
            count += 1
            L = 3
        elif string[0] == 'L':
            L -= 1
        else:
            L = 3
    return recursive_helper(string[1:], count, L)


def class_roster(string):
    """
    Determines whether a student is in
    good standing. (i.e. no more than
    2 A and no more than 2 consecutive L)
    """
    count = 0
    L = 3
    return recursive_helper(string, count, L)


print(class_roster('PAPPALL'))
