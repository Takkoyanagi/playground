def base_conv(num, base):
    """Write a Python program to converting 
    an Integer to a string in any base"""

    _list = []
    if num//base == 0:
        return str(num%base)
    else:
        return (base_conv(num//base, base) + str(num%base))


print(base_conv(100,5))

