s = 'RLLLLRRRLR'
count = 0
output = 0
for i in range(len(s)):
    if s[i] == 'R':
        count += -1
        if count == 0:
            output += 1
    else:
        count += 1
        if count == 0:
            output += 1

print(output)