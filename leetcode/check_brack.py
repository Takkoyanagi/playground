from collections import deque


def check_brach(string):
    """
    Check whether strig has balanced
    brackets
    """
    brackets = {'(': ')', '[': ']', '{': '}'}
    stack = deque()

    for paren in string:
        if paren in brackets:
            stack.append(brackets[paren])
        else:
            if stack and stack[-1] == paren:
                stack.pop()
            else:
                return False
    return False if stack else True


string = '([])((){})'
print(check_brach(string))
