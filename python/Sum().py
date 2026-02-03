#Sum()
"""
Sum of numbers in the list is required everywhere. Python provides an inbuilt function sum() which sums up the numbers in the list.
Syntax:

sum(iterable, start)  
iterable : iterable can be anything list , tuples or dictionaries ,
 but most importantly it should be numbers.
start : this start is added to the sum of 
numbers in the iterable. 
If start is not given in the syntax , it is assumed to be 0.
Possible two syntaxes:

sum(a)
a is the list , it adds up all the numbers in the 
list a and takes start to be 0, so returning 
only the sum of the numbers in the list.
sum(a, start)
this returns the sum of the list + start 


"""


# Python code to demonstrate the working of 
# sum()
numbers = [1,2,3,4,5,6,7,8,9,10]
Sum = sum(numbers)
print(Sum)
#55
print(len(numbers))
#10
print(Sum/len(numbers))
#5.5

Sum2 = sum(numbers,4)
print(Sum2)
#59

# Python code to demonstrate the exception of 
# sum()
arr = ["a"]
  
# start parameter is not provided
Sum = sum(arr)
print(Sum)
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""