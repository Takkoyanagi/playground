def print_reverse(string):
    """
    returns the string in 
    reverse order recursively
    """
    # basecase
    if not string:
        return ""
    else:
        return string[-1] + print_reverse(string[:-1])


print(print_reverse('happy'))
