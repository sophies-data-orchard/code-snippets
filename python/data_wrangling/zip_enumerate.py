# Zip, Enumerate

#  Both enumerate and zip are powerful functions in Python, but they serve different purposes. Here’s a breakdown of when to use each:

# enumerate
# Purpose: Use enumerate when you need to iterate over a sequence (like a list or a string) and you also need to keep track of the index of each item.

# Example:

# Python

# fruits = ['apple', 'banana', 'cherry']
# for index, fruit in enumerate(fruits):
#     print(index, fruit)


# 0 apple
# 1 banana
# 2 cherry

# When to use:

# When you need both the index and the value during iteration.
# When you want to avoid manually managing a counter variable.
# zip
# Purpose: Use zip when you need to iterate over multiple sequences in parallel, combining elements from each sequence into tuples.

# Example:

# Python

# names = ['Alice', 'Bob', 'Charlie']
# ages = [25, 30, 35]
# for name, age in zip(names, ages):
#     print(name, age)

# Output:

# Alice 25
# Bob 30
# Charlie 35

# When to use:

# When you need to iterate over two or more sequences at the same time.
# When you want to pair elements from multiple sequences together.
# Combining enumerate and zip
# You can also combine enumerate and zip if you need to iterate over multiple sequences and keep track of the index:

# Example:

# Python

# names = ['Alice', 'Bob', 'Charlie']
# ages = [25, 30, 35]
# for index, (name, age) in enumerate(zip(names, ages)):
#     print(index, name, age)
# AI-generated code. Review and use carefully. More info on FAQ.
# Output:

# 0 Alice 25
# 1 Bob 30
# 2 Charlie 35

# When to use:

# When you need the index and want to iterate over multiple sequences simultaneously.
# I hope this helps! Do you have any specific use cases in mind where you’re deciding between enumerate and zip? 😊
#  You can use the zip function to combine two lists into a dictionary in Python. Here’s a simple example:

# Example:
# Let’s say you have two lists, one with keys and one with values:

# Python

# keys = ['apple', 'banana', 'cherry']
# values = [1, 2, 3]

# # Using zip to combine lists into a dictionary
# dictionary = dict(zip(keys, values))

# print(dictionary)
# Output:
# {'apple': 1, 'banana': 2, 'cherry': 3}

# Explanation:
# zip(keys, values): This pairs each element from the keys list with the corresponding element from the values list, creating an iterator of tuples.
# dict(zip(keys, values)): The dict constructor takes the iterator of tuples and converts it into a dictionary.
# This method is efficient and concise for creating dictionaries from two lists. Do you have any specific use cases or additional questions about this? 😊








first_name = ['Albert', 'Chris', 'Jen']
last_name = ['Waldron', 'Kinkade', 'Sherwood']
zipped = zip(first_name, last_name)
print(zipped)  #<- Lazy generator
# <zip object at 0x000002C84339B540>

# create a list, using the new "zipped" iterable,tuple is the item of the list
zip_list = list(zipped)
print(zip_list)
# [('Albert', 'Waldron'), ('Chris', 'Kinkade'), ('Jen', 'Sherwood')]

list(zip(first_name, last_name))
# [('Albert', 'Waldron'), ('Chris', 'Kinkade'), ('Jen', 'Sherwood')]

print([name for name in zip_list])
# [('Albert', 'Waldron'), ('Chris', 'Kinkade'), ('Jen', 'Sherwood')]
for i in zipped:
    print(i)
print(list(zipped))
# []
print(zipped)
# <zip object at 0x000002C84339B540>
# Generators in Python are "lazy" iterators, meaning they yield items one at a time and are
# exhausted once they've been fully iterated through. Once a generator is exhausted, you can't
# "rewind" it—you'd have to recreate it if you want to iterate again.
# Here are the main operations that exhaust a generator:
# Operations that Exhaust a Generator: Converting to a list:
# list(generator) will exhaust the generator because it loops through all the values to create alist. 
# python Copy code list(zipped) # This exhausts the generator Using a for loop:
# Iterating over the generator in a for loop consumes its items. python Copy code for item ingenerator: 
# print(item) # After the loop, the generator is empty Calling next() until exhausted:
# Each call to next(generator) fetches one item from the generator. Once all items areconsumed, 
# the generator raises a StopIteration exception. python Copy code next(generator)# Each call 
# exhausts one item Using functions that fully consume the generator:
# Some functions, like sum(), max(), min(), or any(), fully iterate through the generator tocompute 
# their result, exhausting it in the process. python Copy code sum(generator) # Fullyconsumes the 
# generator to sum up values Unpacking:
# If you unpack the generator into variables, like a, b, c = generator, this will also exhaust it.python 
# Copy code a, b, c = zipped # This consumes all elements What Doesn't Exhaust aGenerator: Referencing the generator: 
# Just assigning or referencing a generator doesn’texhaust it. Only when you explicitly loop over or consume it does it get exhausted.
# python Copy code gen = (x for x in range(10)) # This does not exhaust it Re-creating thegenerator: 
# You can recreate the generator as many times as you need. Just remember it’s aone-time use thing.
# Let me know if this clears it up!
# Should we always convert our iterable to a new data structure? Maybe, maybe not.
# Creating a new list from the iterable will use up memory which you might not need.
# You may be able to perform the desired operation on your iterable# without
# creating anew container. Examples include:
# Filtering
# Sorting
# If you need to perform sequence-like operations on the zipped iterables, you will likelyneed to create a new data structure. Examples include:
# Slicing
# Indexing


# unequal length lists, note also that we are also zipping up 3 iterables
seq3 = [1,2]
zip_list = list(zip(first_name,last_name,seq3))
zip_list
# [('Albert', 'Waldron', 1), ('Chris', 'Kinkade', 2)]


# Enumerate
# https://realpython.com/python-enumerate/
# Simplify Loops That Need Counters
# Use enumerate() to get a counter in a loop
# Apply enumerate() to display item counts
# Use enumerate() with conditional statements
# Implement your own equivalent function to enumerate()
# Unpack values returned by enumerate()



for index, value in enumerate(first_name):
    print(index,value)
# 0 Albert
# 1 Chris
# 2 Jen   

# Let's create a list of tuples
enum_list =[]
for pair in enumerate(first_name):
    enum_list.append(pair)
enum_list
# [(0, 'Albert'), (1, 'Chris'), (2, 'Jen')]

# Let's create a dictionary which allows us to check
# what a given element's index is in a sequence
enum_dict ={}
for index, value in enumerate(first_name):
    enum_dict[value] = index
print(enum_dict)
# {'Albert': 0, 'Chris': 1, 'Jen': 2}
print(enum_dict['Jen'])


values = ['a','b','c']
for count, value in enumerate(values):
    print(count, value)
# 0 a
# 1 b
# 2 c 
# 
for count, value in enumerate(values,start = 1):
    print(count, value)
# 1 a
# 2 b
# 3 c
# Keep in mind that enumerate() increments the count by one on every iteration.

users = ["Test User", "Real User 1", "Real User 2"]
for index, user in enumerate(users):
    if index == 0:
        print("Not real user:", user)
    else:
        print(user)
# Not real user: Test User
# Real User 1
# Real User 2

n = [1,2,3,4,5,6,7,8,9]

n=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def even_items(n):
    res = []
    for index, value in enumerate(n, start = 1):
        if not index%2 == 0:
            res.append(value)
    return res
print(even_items(n))
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print([v for i, v in enumerate(n,start =1) if not i%2])
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

import string
str = string.ascii_lowercase
n= 'abcdefghijklmnopqrstuvwxyz'
print(even_items(n))
# ['a', 'c', 'e', 'g', 'i', 'k', 'm', 'o', 'q', 's', 'u', 'w', 'y']

list(n[1::2])
# ['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v', 'x', 'z']

seasons = ["Spring", "Summer", "Fall", "Winter"]
idx =[]
for i in range(len(seasons)):
    idx.append(i)
# print(idx)
# [0, 1, 2, 3]

seasons = ["Spring", "Summer", "Fall", "Winter"]
def my_enumerate(sequence, start=0):
     n = start
     for elem in sequence:
         yield n, elem
         n += 1

list(my_enumerate(seasons))
# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

list(my_enumerate(seasons, start=1))
# [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

# or

indexed_seasons = [(i + 1, season) for i, season in enumerate(seasons)]

print([(i+1,season) for i, season in enumerate(seasons)])
# [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

print([(season,i+1) for i, season in enumerate(seasons)])
# [('Spring', 1), ('Summer', 2), ('Fall', 3), ('Winter', 4)]


