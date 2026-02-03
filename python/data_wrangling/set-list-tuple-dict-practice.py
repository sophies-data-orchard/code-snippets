# Set practicing
thisset = {'apple','banana','cherry'}
mylist = ['apple','kiwi','orange']
thisset.update(mylist)
print(thisset)

set1 = {'a','b','c'}
mylist = ['a',1,2]
mytuple = ('t1',3,'t2','b')
set1.update(mylist)
print(set1) #{1, 2, 'a', 'b', 'c'}

# can add value from any iterable object(tuples,lists, dictionaries etc)
set1.update(mytuple)
print(set1) #{1, 2, 3, 'a', 'b', 'c', 't1', 't2'}
mydict = {'mom':'Sophie', 'dad':'Kevin'}
set1.update(mydict)
print(set1) #{1, 2, 3, 'dad', 'a', 'b', 'c', 'mom', 't1', 't2'}
# add values of dict to set1 by default
set1.update(mydict.values()) #add the values of dict to set
print(set1) 
#{'Sophie', 1, 2, 3, 'dad', 'a', 'b', 'c', 'mom', 't1', 't2', 'Kevin'} 

set1.remove('Sophie')
print(set1) 
#{1, 2, 3, 'dad', 'a', 'b', 'c', 'mom', 't1', 't2', 'Kevin'}

set1.discard('Charles') #discard the non-existant item, no error raised

set1.pop() # remove item randomly:random, random, random
print(set1)
# {2, 3, 'dad', 'a', 'b', 'c', 'mom', 't1', 't2', 'Kevin'}

seta={"a","b","c"}
setb={1,2,3}
setc=seta|setb
print(setc)
# {1, 2, 3, 'a', 'b', 'c'}

set1 = {"a", "b", "test"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "test"}

myset = set1.union(set2, set3, set4)
print(myset)
# {1, 2, 3, 'a', 'Elena', 'b', 'apple', 'test', 'bananas', 'John'}

set1 = {"a", "b", "test"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "test"}

# | is as union()
myset = set1 | set2 | set3 |set4
print(myset)
# {1, 2, 3, 'a', 'Elena', 'b', 'apple', 'test', 'bananas', 'John'}

# set union() the tuple and other datatype
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)
# {1, 2, 3, 'a', 'b', 'c'}

print(len(x))


# Tuple
thistuple = ("apple",)
print(type(thistuple))
# <class 'tuple'>

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
# <class 'str'>

# tuple can have muiltiple datatypes
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
# ('abc', 34, True, 40, 'male')
tuple2 =('abc', 34, True, 40, 'male',{'1':'a'})
print(tuple2)
# ('abc', 34, True, 40, 'male', {'1': 'a'})
print(type(tuple2))
<class 'tuple'>

atuple = ('a','b','c')
print(type(atuple))
# <class 'tuple'>
btuple =(('a','b','c'))
# <class 'tuple'>
print(type(btuple))
ctuple =tuple('a','b','c')
print(type(ctuple))
# NameError: name 'ctuple' is not defined
# use tuple method must use double round-brackets!!!
dtuple =tuple(('a','b','c'))

print(type(dtuple))
# <class 'tuple'>

print(btuple)
# ('a', 'b', 'c')


thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
# banana
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
# cherry
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
# ('cherry', 'orange', 'kiwi')
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
# ('cherry', 'orange', 'kiwi', 'melon', 'mango')
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
# ('orange', 'kiwi', 'melon')
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
#  Yes, 'apple' is in the fruits tuple
#  
# tuple is unchangeable after created.
# workaound: convert to list, change the value, then convert back to tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[0] ='ananas'
x=tuple(y)
print(x)




# Unpacking a tuple:
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
# >>> print(green)
# apple
# >>> print(yellow)
# banana
# >>> print(red)
# cherry


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
# >>> print(green)
# apple
# >>> print(yellow)
# banana
# >>> print(red)
# ['cherry', 'strawberry', 'raspberry']
# >>>
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
# >>> print(green)
# apple
# >>> print(tropic)
# ['mango', 'papaya', 'pineapple']
# >>> print(red)
# cherry
# >>>

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
# apple
# banana
# cherry

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
   print(thistuple[i])
# apple
# banana
# cherry

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
# ('a', 'b', 'c', 1, 2, 3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
# ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

# Search for the first occurrence of the value 8, and return its position:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)
# 3

# Return the number of times the value 5 appears in the tuple:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)
# 2

# list

mylist = ["apple", "banana", "cherry"]
print(type(mylist))
# <class 'list'>

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
# ['apple', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
# ["apple", "banana", "cherry", "orange"]

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
# ['apple', 'blackcurrant', 'cherry']
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
# ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango'] 
print(thislist[4:])
# ['kiwi', 'mango']
print(thislist[-2:])
# ['kiwi', 'mango']
print(thislist[-2:-1])
# ['kiwi']

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(thislist.pop(1))
# banana
print(thislist)
# ['apple', 'cherry']

thislist = ["apple","apple", "banana", "cherry"]
thislist.remove("apple")
print(thislist)

from IPython.display import display
thislist.clear()
display(thislist)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    display(thislist[i])
# apple
# banana
# cherry

# List comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist =[i for i in fruits if 'a' in i]
print(newlist)
# ['apple', 'banana', 'mango']

newlist =[i for i in fruits if 'a' not in i]
print(newlist)
# ['cherry', 'kiwi']

newlist = [x for x in range(10)]
print(newlist)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
newlist = [x for x in range(10) if x < 5]
print(newlist)

newlist = ['hello' for x in fruits]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)
# ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist =[x if x !='banana' else 'orange' for x in fruits]
print(newlist)
# ['apple', 'orange', 'cherry', 'kiwi', 'mango']
# once x = 'banana', then return orange

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
# ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
display(thislist)
# [100, 82, 65, 50, 23]

# Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
# [50, 65, 23, 82, 100]

# Case sensitive sorting can give an unexpected result:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
# ['Kiwi', 'Orange', 'banana', 'cherry']
# Uppercase first letter words are sorted before lowercase words
# want a case-insensitive sort function, use str.lower as a key function:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
# ['banana', 'cherry', 'Kiwi', 'Orange']

# reverse the order of a list, regardless of the alphabet
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
# ['cherry', 'Kiwi', 'Orange', 'banana']

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
display(mylist)
# ['apple', 'banana', 'cherry']

# list() method
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
# ['apple', 'banana', 'cherry']

# make a copy of a list by using the : (slice) operator.
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
# ['apple', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
display(thislist[::-1])
# ['cherry', 'banana', 'apple']

thislist = ["apple", "banana", "cherry", 1,2,3]
# get last 3 items
display(thislist[-3:])
# [1, 2, 3]
# get last 3 items in reverse
display(thislist[-1:-4:-1])
# [3, 2, 1]
#get last 3 items, then reverse
display(thislist[-3:][::-1])
# [3, 2, 1]
# reverse the list first, then get the first 3 items
display(thislist[::-1][:3])
# [3, 2, 1]

# dictionary
# Constructing a new Dictionary
dictionary1 = {} # Curly braces method
dictionary2 = dict() # Dict method

# Populate the dictionary
dictionary1["key1"] = "value1"
dictionary1["key2"] = "value2"
print(f"Dictionary 1: {dictionary1}")
# Dictionary 1: {'key1': 'value1', 'key2': 'value2'}
dictionary2["key1"] = "value1"

print(f"Dictionary 2: {dictionary2}")
# Dictionary 1: {'key1': 'value1'}
# Dictionary 2: {'key1': 'value1'}

d1 = {}
d1['mom']='sophie'
d1['dad']='kevin'
print(f'd1:{d1}')
# d1:{'mom': 'sophie', 'dad': 'kevin'}
d2 = {}
d2['son1']='Charles'
d2['son2']='Henry'
print(f'd2:{d2}')
# d2:{'son1': 'Charles', 'son2': 'Henry'}

# create dict
d1 = dict(a=11, b=21)
print(d1)
# {'a': 11, 'b': 21}

d3 ={}
d3 = {'mom': 'sophie', 'dad':'kevin'} # key and values must have the round brackets
print(d3)
# {'mom': 'sophie', 'dad': 'kevin'}
d4 = {}
d4 = {4:'t1',5:'t2'}
print(d4)
# {4: 't1', 5: 't2'}
d5 = {}
d5 = {'4':'t1','5':'t2'}
print(d5)
# {'4': 't1', '5': 't2'}

# dict iterate
harry_potter_dict = {
    "Harry Potter": "Gryffindor",
    "Ron Weasley": "Gryffindor",
    "Hermione Granger": "Gryffindor",
    "Draco Malfoy": "Slytherin"
}

for k in harry_potter_dict:
   v = harry_potter_dict[k]
   print(f'{k} is in {v} .')

for k in harry_potter_dict:
   v = harry_potter_dict[k]
   print(f'{k} is from {v}.')
#    Harry Potter is in Gryffindor .
# Ron Weasley is in Gryffindor .
# Hermione Granger is in Gryffindor .
# Draco Malfoy is in Slytherin .

for k in harry_potter_dict:
   v = harry_potter_dict[k]
   print(f'I love {k} from {v} *_*')
# I love Harry Potter from Gryffindor *_*
# I love Ron Weasley from Gryffindor *_*
# I love Hermione Granger from Gryffindor *_*
# I love Draco Malfoy from Slytherin *_*




# Get the lenth of the key
print(len(harry_potter_dict))
# 4

# Is Harry Potter one of the keys?
print("Harry Potter" in harry_potter_dict)
# True
print("Elisa" in harry_potter_dict)
False
# Assign a new value to a key, old value will be replaces
harry_potter_dict['Draco Malfoy'] ='TBD'
print(harry_potter_dict)
# {'Harry Potter': 'Gryffindor', 'Ron Weasley': 'Gryffindor', 
# 'Hermione Granger': 'Gryffindor', 'Draco Malfoy': 'TBD'}

# This is a helper function for printing our dictionaries
from pprint import pprint
harry_potter_dict = {
    "Harry Potter": "Gryffindor",
    "Ron Weasley": "Gryffindor",
    "Hermione Granger": "Gryffindor",
    "Draco Malfoy": "Slytherin"
}
# Custom printer (ignore)
def pretty_print(text):
    print(text)
    pprint(harry_potter_dict)

# Display the dictionary
pretty_print("Starting Dictionary: ")
print(harry_potter_dict)

# Starting Dictionary:
# {'Draco Malfoy': 'Slytherin',
#  'Harry Potter': 'Gryffindor',
#  'Hermione Granger': 'Gryffindor',
#  'Ron Weasley': 'Gryffindor'}
# >>> print(harry_potter_dict)
# {'Harry Potter': 'Gryffindor', 'Ron Weasley': 'Gryffindor', 'Hermione Granger': 'Gryffindor', 'Draco Malfoy': 'Slytherin'}

harry_potter_dict = {
    "Harry Potter": "Gryffindor",
    "Hermione Granger": "Gryffindor"
}
add_characters_1 = {
    "Al": "Gr",
    "Lu": "Ra"
}
# Use iterables to update a dictionary
add_characters_2 = [
    ["Dr", "Sl"],
    ["Ce", "Hu"]
    # ["Harry Potter": "Gryffindor",]
]
harry_potter_dict.update(add_characters_1)
harry_potter_dict.update(add_characters_2)

# Display the dictionary
pretty_print("After Method 2:")

add_characters_3 = {"Harry Potter": "GG"}
harry_potter_dict.update(add_characters_3)
pretty_print("After Method 3:")
# {'Al': 'Gr',
#  'Ce': 'Hu',
#  'Dr': 'Sl',
#  'Harry Potter': 'GG',
#  'Hermione Granger': 'Gryffindor',
#  'Lu': 'Ra'}
# ---> Harry Portter's value has been altered.

harry_potter_dict = {
    "Harry Potter": "Gryffindor",
    "Hermione Granger": "Gryffindor"
}
#  METHOD 3 ------------------------------------------------------------
# Adding a new character, but only if the key doesn't already exist
# setdefault only use when the key doesn't exist
harry_potter_dict.setdefault("Rubeus Hagrid", "Gryffindor")

# Let's try to add a character to the wrong house
harry_potter_dict.setdefault("Harry Potter", "Slytherin")

# Display the dictionary (Notice Harry Potter's House hasn't changed)
pretty_print("After Method 3:")
# {'Harry Potter': 'Gryffindor',
#  'Hermione Granger': 'Gryffindor',
#  'Rubeus Hagrid': 'Gryffindor'}


# the setdefault method can prevent key-value remapping 
# in a dictionary. When you use setdefault, it only sets 
# the value for a key if that key is not already present 
# in the dictionary. If the key is already present, 
# setdefault will not change its value.

# del
if "Ron Weasley" in harry_potter_dict:
    del harry_potter_dict["Ron Weasley"]
# Display the dictionary
pretty_print("After Method 1:")
# with the if clause, there is not error throwing 

# After Method 1:
# {'Harry Potter': 'Gryffindor',
#  'Hermione Granger': 'Gryffindor',
#  'Rubeus Hagrid': 'Gryffindor'}


# throw error it the key doesn't exist
del harry_potter_dict["Ron Weasley"]
# KeyError: 'Ron Weasley'

harry_potter_dict.pop("Draco Malfoy", None)

# change the value
# value here is the list
fruits_list = ['a','b','c']
food_type ={
   "fruits":fruits_list

}
fruits_list.append('dd')
food_type["fruits"].append("cc")
# food_type["fruits_list"].append("cc") 
print(food_type)
# {'fruits': ['a', 'b', 'c', 'dd', 'cc']}

print(harry_potter_dict.keys())
# dict_keys(['Harry Potter', 'Ron Weasley', 'Hermione Granger'])
print(harry_potter_dict.values())
# dict_values(['Gryffindor', 'Gryffindor', 'Gryffindor'])
print(harry_potter_dict.items())
# dict_items([('Harry Potter', 'Gryffindor'), ('Ron Weasley', 'Gryffindor'), ('Hermione Granger', 'Gryffindor')])

for key, value in harry_potter_dict.items():
   display(key)
   display(value)
   print('\n')

# Harry Potter
# Gryffindor

# Ron Weasley
# Gryffindor


# Hermione Granger
# Gryffindor

from collections import Counter
s = "bbbaaaabaaa"
# Create the counter
count = Counter(s)
print ('Initial :', count)
# Initial : Counter({'a': 7, 'b': 4})
# We can add to it by supplying a new iterable and using .update()
count.update('abcdaab')
print ('Updated:', count)
# Updated: Counter({'a': 10, 'b': 6, 'c': 1, 'd': 1})

# If a value hasn't occurred, our counter won't throw an error!
# Counter is a dictionary
print('How many times have we seen the letter "z"? ', count["z"])
# 0
count.get('d')
# 1
count.get('a')
# 10



# defaultdict
harry_potter_dict = {
    "Harry Potter": "Gryffindor",
    "Ron Weasley": "Gryffindor",
    "Hermione Granger": "Gryffindor",
    "Luna Lovegood": "Ravenclaw",
    "Draco Malfoy": "Slytherin",
    "Cedric Diggory": "Hufflepuff"
}
# Now, create a default dictionary
harry_potter_default = defaultdict(str, harry_potter_dict)
display(harry_potter_default)

# What happens if we try to index on a non-existent key?
print("Dumbledore's house is:", harry_potter_default["Albus Dumbeldore"])
display(harry_potter_default)

# defaultdict(str,
#             {'Harry Potter': 'Gryffindor',
#              'Ron Weasley': 'Gryffindor',
#              'Hermione Granger': 'Gryffindor',
#              'Luna Lovegood': 'Ravenclaw',
#              'Draco Malfoy': 'Slytherin',
#              'Cedric Diggory': 'Hufflepuff'})
# Dumbledore's house is: 
# defaultdict(str,
#             {'Harry Potter': 'Gryffindor',
#              'Ron Weasley': 'Gryffindor',
#              'Hermione Granger': 'Gryffindor',
#              'Luna Lovegood': 'Ravenclaw',
#              'Draco Malfoy': 'Slytherin',
#              'Cedric Diggory': 'Hufflepuff',
#              'Albus Dumbeldore': ''})  
#
# Last line<-- Dumbeldore doesn't exist in dict harry_potter_default
# defaultdict create a dict returns to let us index a not exist key
