# defaultdict

from collections import defaultdict
s = "mississippi"
d = defaultdict(int)
for k in s:
    d[k] += 1
sorted(d.items())
# output
# [('i', 4), ('m', 1), ('p', 2), ('s', 4)]

from collections import defaultdict
s = [('yellow',1),('blue',2),('yellow',3),('blue',4),('red',1)]
d = defaultdict(list)
for k,v in s:
    d[k].append(v)
sorted(d.items())
# output:
# [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
