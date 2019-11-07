from collections import deque
 #initiate deque
dq = deque()

def palindrome(string):
    """determines whether a string
    is a palindrome"""
    # ensure item provided is not a string
    if not isinstance(string, str):
        return 'Not a string'
    for letter in string:
        dq.append(letter)
    while (len(dq) > 1):
        right = dq.pop()
        left = dq.popleft()
        if right != left:
            return False
    return True

print(palindrome('mom'))
