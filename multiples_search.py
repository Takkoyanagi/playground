# find the number that is repeated
# length is n + 1 and (1,n)
import math 
array = [1,2,3,4,5,6,10,8,8,8,8]
n = 10
x = (n + 1)//2

def find_mult(array, n, h=0,l=0):
    # x = (n+1)//2
    for i in array:
        if i < x:
            l += 1
        elif i > x:
            h += 1
    if (l + h <= x) | (l == x-1 and h == n-x):
        return x
    elif l > h:
        return left()
    elif l < h:
        return right()

def left(l=0, h=0, x=x-(x-1)//2):
    if x == 1:
        return 1
    else: 
        for i in array:
            if i < x:
                l += 1
            elif i > x:
                h += 1
        if l+h <= x:
            return x
        else:
            return left(x=x-math.ceil((x-1)/2))


def right(l=0,h=0,x=x+math.ceil((n-x)/2)):
    if x == n:
        return n
    else: 
        for i in array:
            if i < x:
                l += 1
            elif i > x:
                h += 1
        if l + h <= x:
            return x
        else:
            return right(x=x+math.ceil((n-x)/2))

print(find_mult(array,n=n))