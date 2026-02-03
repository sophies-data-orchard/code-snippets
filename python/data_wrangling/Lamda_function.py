# Lamda function

result = lambda x:x*2
print(result(9))
# 18

r2 = lambda x: x**5
print(r2(2))
# 32
print(r2(10))
# 100000

# lambda function w/0 name, so it's call anonomous name
print(result)
# <function <lambda> at 0x000001B797E9C310>

# use case
# map()
# filter()
# itertools.reduce()
# sorted()

demo_tuple = (1, 2, 3, 4, 5)
squared_val=map(lambda x:x**2, demo_tuple)
print(tuple(squared_val))
# (1, 4, 9, 16, 25)


# map()

def fun(a):
    return len(a)
x = map(fun, ('dad','grand','lake'))

print(x)
# <map object at 0x000001B7988B19D0>

print(list(x))
# [3, 5, 4]

def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(list(x))
# ['appleorange', 'bananalemon', 'cherrypineapple']


# filter()

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)
...
# 18
# 24
# 32

# a list contains both even and odd numbers. 
seq = [0, 1, 2, 3, 5, 8, 13]

# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))
# [1, 3, 5, 13]
# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))
# [0, 2, 8]