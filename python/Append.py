# Append
# 1)
level = [[1],[2,3],[4,5,6]]
new =[7,8,9,10]
level.append(new)
print(level)
# #output
# [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]

# 2)
level = [[1],[2,3],[4,5,6]]
new =[[7,8,9,10],[11,12],[13,14]]
for i in new:
    level.append(new)
print(level)
# output: it's obvious the result that I didn't want
# [[1], [2, 3], [4, 5, 6], [[7, 8, 9, 10], [11, 12], [13, 14]], [[7, 8, 9, 10], [11, 12], [13, 14]], [[7, 8, 9, 10], [11, 12], [13, 14]]]

# 3)
level = [[1],[2,3],[4,5,6]]
new =[[7,8,9,10],[11,12],[13,14]]
for i in new:
    level.append(i)
print(level)
# ouput
# [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10], [11, 12], [13, 14]]