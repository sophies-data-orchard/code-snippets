# Walrus operator in Python 3.8
"""
Walrus-operator is another name for assignment expressions. 
According to the official documentation, it is a way to assign to variables
 within an expression using the notation NAME := expr. The Assignment 
 expressions allow a value to be assigned to a variable, even a variable 
 that doesn’t exist yet, in the context of expression rather than as a 
 stand-alone statement.
"""


a = [1, 2, 3, 4]
if (n := len(a)) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")

# output
# List is too long (4 elements, expected <= 3)


sample_data = [
    {"userId": 1,  "name": "Matthew", "completed": False},
    {"userId": 1, "name": "Mark", "completed": False},
    {"userId": 1,  "name": "Luke", "completed": False},
    {"userId": 1,  "name": "John", "completed": True}
]
print("With Python 3.8 Walrus Operator:") 
for entry in sample_data: 
    if name := entry.get("name"):
        print(f'Found name: "{name}"')
# output
# With Python 3.8 Walrus Operator:
# Found name: "Matthew"
# Found name: "Mark"
# Found name: "Luke"
# Found name: "John"

print("Without Walrus operator:")
for entry in sample_data:
    name = entry.get("name")
    if name:
        print(f'Found name: "{name}"')   
         
# output
# Without Walrus operator:
# Found name: "Matthew"
# Found name: "Mark"
# Found name: "Luke"
# Found name: "John"


# example A
# w/o walrus operator
nums = [10,20,30,40,50]
if len(nums):
    print(f"There are {len(nums)} elements in the list")

nums = [10,20,30,40,50]
size = len(nums)
if size:
    print(f"There are {size} elements in the list")
# output
# There are 5 elements in the list

# w walrus operator
nums = [10,20,30,40,50]
if (size:=len(nums)):
    print(f"There are {size} elements in the list")
# output
# There are 5 elements in the list   


