op = 0
S = "()(())"
a = ""
for i in S:
    if i == '(' and op > 0:
        a += i
    elif i == ')' and op > 1:
        a += i
    op += 1 if i == '(' else -1
print(a)
