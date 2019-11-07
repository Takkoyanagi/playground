from stack import Stack

def postfix(infix_op):
    """Converts operation to postfix from a given 
    set of mathematical equation"""

    prec = {}
    prec['/'] = 3
    prec['*'] = 3
    prec['-'] = 2
    prec['+'] = 2
    prec['('] = 1
    stack = Stack()
    _list = []
    tokens = infix_op.split()

    for token in tokens:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
        or token in '1234567890':
            _list.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            top_pop = stack.pop()
            while top_pop != '(':
                _list.append(top_pop)
                top_pop = stack.pop()
        else:
            while (not stack.isEmpty()) \
            and (prec[stack.peek()] >= prec[token]):
                _list.append(stack.pop())
            stack.push(token)

    while not stack.isEmpty():
        _list.append(stack.pop())
    return " ".join(_list)

infix_op = '( A + B ) * ( C + D )'


print(postfix(infix_op))
# output should be ABC*+
