left = 1
right = 22

# num = [128, 1, 10, 25, 24]
# a = []
# for item in range(left, right+1):
#     for indx, i in enumerate(list(str(item))):
#         if i == '0':
#             break
#         elif item % int(i) != 0:
#             break
#         elif indx == len(list(str(item)))-1:
#             a.append(item)

# print(a)


print([x for x in range(left, right+1) if all(int(i) != 0 and x %
                                              int(i) == 0 for i in str(x))])
