from stack import Stack
s = Stack()
def base_conv_stack(num, base):
    """ converts a number to a base other
    than 10
    num = number in base 10
    base = base to change to"""
  
    s.push(num % base)
    #print(s.peek())
    if num != 0:
        return base_conv_stack(num//base, base)
    
    number = ""
    while (not s.isEmpty()):
        number += str(s.pop())
    return number

print(base_conv_stack(100, 5))
