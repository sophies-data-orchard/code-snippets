numbers = [2,4,6,8,10]
def square(number):
    return number * number
squared_numbers = list(map(square,numbers))
print(squared_numbers)


# output:
# [4, 16, 36, 64, 100]

"""
map() Syntax
Its syntax is:

map(function, iterable, ...)

map() Parameter
The map() function takes two parameters:

function - a function that perform some action to each element of an iterable
iterable - an iterable like sets, lists, tuples, etc
You can pass more than one iterable to the map() function.

""""