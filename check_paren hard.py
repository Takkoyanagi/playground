from stack import Stack
def is_paren(string):
    """ Determines whether parenthesis are balanced
    """
    s = Stack()
    balanced = True
    index = 0
    while (index < len(string)) & balanced:
        symbol = string[index]
        if symbol in '({[':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1

    if balanced and s.isEmpty():
        return True
    else: 
        return False

def matches(left, right):
    _open = ['(','[','{']
    _close = [')',']','}']
    return _open.index(left) == _close.index(right)

print(is_paren('([])'))