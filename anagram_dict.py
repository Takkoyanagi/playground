def anagram(string1, string2):
    """Determines whether two strings 
    provided are anagrams O(1)"""
    dict_1 = {}
    dict_2 = {}
    for i in string1:
        if i not in dict_1:
            dict_1[i] = 1
        else:
            dict_1[i] += 1
    for j in string2:
        if j not in dict_2:
            dict_2[j] = 1
        else:
            dict_2[j] += 1
    if dict_1 != dict_2:
        return False
    else:
        return True

print(anagram('abcde', 'edbca'))