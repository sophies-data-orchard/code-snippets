first_name = ['Albert', 'Chris', 'Jen','boom']
last_name = ['Waldron', 'Kinkade', 'Sherwood']
zipped = list(zip(first_name, last_name))
print(zipped)
# [('Albert', 'Waldron'), ('Chris', 'Kinkade'), ('Jen', 'Sherwood')]

# Yes, you can zip two lists of different lengths in Python,
#  but the behavior depends on the method you use.

# Using the built-in zip() function: This function stops creating pairs 
# when the shortest input iterable is exhausted. For example:
# Python

list1 = [1, 2, 3]
list2 = ['a', 'b']
zipped = list(zip(list1, list2))
print(zipped)  # Output: [(1, 'a'), (2, 'b')]

first_name = ['Albert', 'Chris']
last_name = ['Waldron', 'Kinkade', 'Sherwood']
zipped = list(zip(first_name, last_name))
print(zipped)
# >>> print(zipped)
# [('Albert', 'Waldron'), ('Chris', 'Kinkade')]
# >>>

Using itertools.zip_longest(): This function allows you to zip lists of different lengths by filling in missing values with a specified fill value:
Python

from itertools import zip_longest

list1 = [1, 2, 3]
list2 = ['a', 'b']
zipped = list(zip_longest(list1, list2, fillvalue=None))
print(zipped)  # Output: [(1, 'a'), (2, 'b'), (3, None)]

# Cycling the shorter list: If you want to cycle through the shorter list until the longer list is exhausted, you can use itertools.cycle():
# Python

from itertools import cycle

list1 = [1, 2, 3, 4]
list2 = ['a', 'b']
zipped = list(zip(list1, cycle(list2)))
print(zipped)  # Output: [(1, 'a'), (2, 'b'), (3, 'a'), (4, 'b')]
# >>> print(zipped)  # Output: [(1, 'a'), (2, 'b'), (3, 'a'), (4, 'b')]
# [(1, 'a'), (2, 'b'), (3, 'a'), (4, 'b')]


dict ={'a':1, 'b':2, 'c':3}
for k,v in dict.items():
    # print(v)
    print(k)
 
# print(v)
# 1
# 2
# 3 
# print(k)
# a
# b
# c
key_list = [1, 2, 3, 4]
value_list = ['a', 'b']
mapping ={}
for k, v in zip(key_list,value_list):
    mapping[k] = v
print(mapping)
# {1: 'a', 2: 'b'}

v = [1,2,3,4,5,6,7,8]
r = v[:-1:2]
print(r)

s = 'deadbeef'
r = int(s,base = 16)
print(r)

s = '3'
fl = int(s,base = 10)
print(fl)

s = '3'
fl = int(s,base = 10)
print(fl)

