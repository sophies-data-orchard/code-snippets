fruits = ['apple','red','apple','red','red','pear']

c = {}
for i in fruits:    
    c[i] = c.get(i,0) + 1
print(c)

# answer: {'apple': 2, 'red': 3, 'pear': 1}

from collections import defaultdict
s = "mississippi"
d = defaultdict(int)
for k in s:
    d[k] += 1
sorted(d.items())
# output
# [('i', 4), ('m', 1), ('p', 2), ('s', 4)]

