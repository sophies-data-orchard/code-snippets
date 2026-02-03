from collections import defaultdict

dd = defaultdict(int)  # Default value is 0 for missing keys
print(dd["non_existent_key"])  # Output: 0

student = {"name": "John Doe", "age": 20}
print(student["name"])  # Output: John Doe
print(student["grade"])  # Raises KeyError: 'grade'


# Example 1: Counting Elements
# You can use defaultdict to count the occurrences of elements in a list.
from collections import defaultdict

# List of items
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# Create a defaultdict with int as the default factory
item_count = defaultdict(int)
# Count each item
for item in items:
    item_count[item] += 1
print(item_count)
# Output: defaultdict(<class 'int'>, {'apple': 3, 'banana': 2, 'orange': 1})
# Count the item in the list, can be used with Counter, which is easier
from collections import Counter
dict(Counter(items))
# {'apple': 3, 'banana': 2, 'orange': 1}

# Example 2: Grouping Items
# You can use defaultdict to group items by a certain property.
from collections import defaultdict
# List of tuples (name, subject)
students = [('Alice', 'Math'), ('Bob', 'Science'), ('Alice', 'Science'), ('Bob', 'Math')]

# Create a defaultdict with list as the default factory
subjects = defaultdict(list)
# subjects = defaultdict(int)

# Group students by subject
for name, subject in students:
    subjects[subject].append(name)

print(subjects)
# Output: defaultdict(<class 'list'>, {'Math': ['Alice', 'Bob'], 'Science': ['Bob', 'Alice']})