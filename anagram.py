def anagram(string1, string2):
    """Determines whether two strings provided are anagrams"""
    # create a list of letters in string, then sort
    s1 = sorted(list(string1))
    s2 = sorted(list(string2))
    
    if len(s1) != len(s2):
        return False
    else:
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return False
            else:
                return True
print(anagram('abcde', 'edca'))