# Index 
# List all the index for each element in the list

# use enumerate
vow = ['a','b','c','d','e']
for index,val in enumerate(vow):
    print(val,index)

#w/o enumerate
vow = ['a','b','c','d','e']
for index in range(len(vow)):
    val = vow[index]
    print(index,val)

