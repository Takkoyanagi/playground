from stack import Stack
def is_paren(string):
    """ Determines whether parenthesis are balanced
    """
    s = Stack()
    balanced = True
    index = 0
    while (index < len(string)) & balanced:
        symbol = string[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index = index + 1

    if balanced and s.isEmpty():
        return True
    else: 
        return False

print(is_paren('()((()'))