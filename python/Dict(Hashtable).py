#Dict
# None key
test = {}
test[None] = 0
test.get(None)

# output
# 0

# print key-value pairs
test ={None:0, 'a':5, 'b':6, 'c':7}
for key,value in test.items():
    print(key,':',value) 

# output
# None : 0
# a : 5
# b : 6
# c : 7

test ={None:0, 'a':5, 'b':6, 'c':7}
print(len(test))
# output:
# 4



#count the items from array as key and save to dict
fruits = ['apple','red','apple','red','red','pear']

c = {}
for i in fruits:    
    c[i] = c.get(i,0) + 1
print(c)
# output
# {'apple': 2, 'red': 3, 'pear': 1}


# count the nodes' val from linked list as key and save to dict
dict = {}
cur = head
while cur:
    if cur.val not in dict:
        dict[cur.val]=0
    print(dict)
    dict[cur.val]+=1
    print(dict)
    cur = cur.next 
return dict

# head: [3,2,2,1,3,2,4]
# result:
# dict: {3: 2, 2: 3, 1: 1, 4: 1} 
process of the above code:
{3: 0}
{3: 1}
{3: 1, 2: 0}
{3: 1, 2: 1}
{3: 1, 2: 1}
{3: 1, 2: 2}
{3: 1, 2: 2, 1: 0}
{3: 1, 2: 2, 1: 1}
{3: 1, 2: 2, 1: 1}
{3: 2, 2: 2, 1: 1}
{3: 2, 2: 2, 1: 1}
{3: 2, 2: 3, 1: 1}
{3: 2, 2: 3, 1: 1, 4: 0}
{3: 2, 2: 3, 1: 1, 4: 1}
