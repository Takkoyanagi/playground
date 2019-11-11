def to_hash(string):
    """converts strings to hash
    t_size = size of hash table
    default is set to 25"""
    prod = 0
    # convert letters to ordinal values
    # then hash by taking modulo
    for pos in range(len(string)):
        prod += int(ord(string[pos]))

    return prod


def anagram(string1, string2):
    """determines whether a strings are anagrams"""
    return to_hash(string1) == to_hash(string2)


print(anagram('apple', 'pcple'))
