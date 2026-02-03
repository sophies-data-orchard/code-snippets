# join
"""
Python String join() Method

Difficulty Level : Basic
Last Updated : 19 Apr, 2022
Python String join() method is a string method and returns a string in which the elements of the sequence have been joined by the str separator.

Syntax: 

string_name.join(iterable) 

Parameters: 

The join() method takes iterable – objects capable of returning their members one at a time. Some examples are List, Tuple, String, Dictionary, and Set

Return Value: 

The join() method returns a string concatenated with the elements of iterable. 

Type Error:

If the iterable contains any non-string values, it raises a TypeError exception. 

"""

l1 = ['1','2','3','4']
s = '-'
s = s.join(l1)
print(s)
# output
# 1-2-3-4

l2 = ['h','e','l','l','o']
print(''.join(l2))
# Output
# hello
