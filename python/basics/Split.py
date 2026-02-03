# split
"""
split() method in Python split a string into a list of strings after
breaking the given string by the specified separator.
string -> a list of strings
Syntax : str.split(separator, maxsplit)

Parameters :
separator : This is a delimiter. The string splits at this specified separator. If is not provided then any white space is a separator.

maxsplit : It is a number, which tells us to split the string into maximum of provided number of times. If it is not provided then the default is -1 that means there is no limit.

Returns : Returns a list of strings after breaking the given string by the specified separator.

"""

# Example 1: Example to demonstrate how split() function works
text = 'geeks for geeks' 
# Splits at space
print(text.split())
# output
# ['geeks', 'for', 'geeks']

word = 'geeks, for, geeks' 
# Splits at ','
print(word.split(','))
# output

# ['geeks', 'for', 'geeks']
word = 'geeks:for:geeks'
  
# Splitting at ':'
print(word.split(':'))
# output
# ['geeks', 'for', 'geeks']

word = 'CatBatSatFatOr'
  
# Splitting at t
print(word.split('t'))

# Example 2: Example to demonstrate how split() function works when maxsplit is specified
word = 'geeks, for, geeks, pawan'
  
# maxsplit: 0
print(word.split(', ', 0))
# output
# ['geeks, for, geeks, pawan']

# maxsplit: 4
print(word.split(', ', 4))
# output
# ['geeks', 'for', 'geeks', 'pawan']
  
# maxsplit: 1
print(word.split(', ', 1))
# ['geeks', 'for, geeks, pawan']