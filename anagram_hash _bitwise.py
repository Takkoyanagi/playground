def to_hash(string):
    """converts strings to hash
    t_size = size of hash table
    default is set to 25"""
    xor = 0
    # convert letters to ordinal values
    # then hash by taking modulo
    for ind in range(len(string)):
        xor ^= int(ord(string[ind]))

    return xor


def anagram(string1, string2):
    """determines whether a strings are anagrams"""
    return to_hash(string1 + string2) == 0


print(anagram('apple', 'paple'))
