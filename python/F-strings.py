# f-strings
"""
PEP 498 introduced a new string formatting mechanism known as Literal String Interpolation 
or more commonly as F-strings (because of the leading f character preceding the string 
literal). The idea behind f-strings is to make string interpolation simpler. 
To create an f-string, prefix the string with the letter “ f ”. The string itself 
can be formatted in much the same way that you would with str.format(). 
F-strings provide a concise and convenient way to embed python expressions inside string 
literals for formatting. 

Note : 

F-strings are faster than the two most commonly used string formatting mechanisms, which are % formatting and str.format(). 

"""

# Python3 program introducing f-string
val = 'Leet'
print(f"{val} for {val} is a portal for {val}.")
# output
# Leet for Leet is a portal for Leet. 

name = "Sophie"
age = 15
print(f"Hello, My name is {name} and I'm {age} years old.")
# output
# Hello, My name is Sophie and I'm 15 years old.


# Prints today's date with help of datetime library
import datetime
 
today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")
print(f"{today: %m-%d-%y}")
output:
# June 02, 2022
# 06-02-22

# Backslash Cannot be used in format string directly.