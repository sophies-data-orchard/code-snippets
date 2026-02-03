#Extend vs append

# Append: Adds its argument as a single element to the end of a list. 
# The length of the list increases by one.
# 1
listA = ['hello','my']
listA.append('darling')
print(listA)
# output 
# ['hello', 'my', 'darling']

# 2
# NOTE: A list is an object. If you append another list onto a list, 
# the parameter list will be a single object at the end of the list.
listA = ['hello','my']
listB = [2,0,2,2]
listA.append(listB)
print(listA)
# Output
# ['hello', 'my', [2, 0, 2, 2]]

# extend(): Iterates over its argument and adding each element to the list and extending the list. 
# The length of the list increases by number of elements in it’s argument.
# 3
listA = ['hello','my']
listB = [2,0,2,2]
listA.extend(listB)
print(listA)
# Output
# ['hello', 'my', 2, 0, 2, 2]

# 4
# NOTE: A string is an iterable, so if you extend a list with a string, 
# you’ll append each character as you iterate over the string.

listA = ['hello','my']
listA.extend('darling')
print(listA)
# Output
# ['hello', 'my', 'd', 'a', 'r', 'l', 'i', 'n', 'g']


# Time Complexity:
# Append has constant time complexity i.e.,O(1).
# Extend has time complexity of O(k). Where k is the length of list which need to be added.


# https://www.geeksforgeeks.org/append-extend-python/#:~:text=If%20you%20append%20another%20list,the%20end%20of%20the%20list.&text=extend()%3A%20Iterates%20over%20its,of%20elements%20in%20it's%20argument.