def roman_to_num(string):
    """returns the numerical representation
    of the roman numeral
    """

    # define numerical mapping to roman numerals
    roman_dic = {'I': 1, 'V': 5, 'X': 10,
                 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # keep cumsum of nums
    total = 0

    for index, val in enumerate(string[:-1]):
        if roman_dic[val] < roman_dic[string[index+1]]:
            total -= roman_dic[val]
        else:
            total += roman_dic[val]
    total += roman_dic[string[-1]]
    return total


print(roman_to_num('MCMXCIV'))
