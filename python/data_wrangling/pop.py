x = [5,3,-4,20,2,9,0,-1]
def foo(z):
    print(x)
    z.pop() #remove last element from z
    print(z)
foo(x)
print(x)

x_float = float(1)
print(x_float)

x = [5,3,-4,20,2,9,0,-1]
def cumulative_sum_v0(x):
    y = []
    for i in range(len(x)):
        s=0
        for k in range(i+1):
            s+=x[k]
        y.append(s)
    return y

print(cumulative_sum_v0(x))


def strcat_list(L):
    assert type(L) is list
    ###
    ### YOUR CODE HERE
    ###
    temp = []
    for i in range(len(L)):
        temp.append(L.pop())
    str = ''.join(temp) #abcdefghi
    return str

L=['abc','def','ghi']
print(strcat_list(L))

def is_number(x):
    """Returns `True` if `x` is a number-like type, e.g., `int`, `float`, `Decimal()`, ..."""
    from numbers import Number
    return isinstance(x, Number)

def floor_fraction(a, b):
    assert is_number(a) and a >= 0
    assert is_number(b) and b > 0
    ###
    ### YOUR CODE HERE
    ###
    x=floor(a/b)
    return x

a=2
b=3
print(floor_fraction(a, b))

# Python3 program introducing f-string
val1 = 'Covid'
val2 ='positive'
print(f"I have {val1} {val2}!")


name = 'Om'
age = 22
print(f"Hello, My name is {name} and I'm {age} years old.")


def count_word_lengths(s):
    assert all([x.isalpha() or x == ' ' for x in s])
    assert type(s) is str
    ###
    ### YOUR CODE HERE
    ###
    new_s = ' '.join(s.split())  #remove multiple spaces in string and rejoin with only 1 space. output:the quick brown fox jumped over the lazy dog
    new_s_list = new_s.split() #convert to list: ['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']
    return [len(i) for i in new_s_list ] #get the length of each word and save to an array : [3, 5, 5, 3, 6, 4, 3, 4, 3]
s = 'the quick  brown   fox jumped over     the lazy  dog'
print(count_word_lengths(s))

# sort 2nd item from tuple, output the sorted list
data = [(1, 'banana'), (2, 'orange'),(3, 'apple')]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)
# output
# [(3, 'apple'), (1, 'banana'), (2, 'orange')]

# sort by the 2nd item in the tuple, output the sorted 2nd item to the list
data = [(1, 'banana'), (2, 'cherry'),(3, 'apple')]
sorted_data = sorted(data, key = lambda x:x[1], reverse = True)
result = [x[1] for x in sorted_data]
print(result)  #['cherry', 'banana', 'apple']

# sort by the second item in the tuple, output the 1st item per the sorting
data = [(1, 'banana'), (2, 'cherry'),(3, 'apple')]
sorted_data = sorted(data, key = lambda x:x[1], reverse = True)
result = [x[0] for x in sorted_data]
print(result)  #[2, 1, 3]


sorted(inputdata, key = lambda, x:x[ind] or item:item[ind])


thisset = {'apple','banana','cherry'}
for x in thisset:
    print(x)
# banana
# apple
# cherry
print('banana' not in thisset)
thisset.add("orange")
print(thisset)

tropical = {"pineapple","mango","papaya"}
thisset.update(tropical)
print(thisset)
# {'cherry', 'apple', 'papaya', 'orange', 'pineapple', 'banana', 'mango'}

thisset = {'apple','banana','cherry'}
mylist = ['apple','kiwi','orange']
thisset.update(mylist)
print(thisset)

set1 = {'a','b','c'}
mylist = ['a',1,2]
mytuple = ('t1',3,'t2','b')
set1.update(mylist)
print(set1) #{1, 2, 'a', 'b', 'c'}
set1.update(mytuple)
print(set1) #{1, 2, 3, 'a', 'b', 'c', 't1', 't2'}
mydict = {'mom':'Sophie', 'dad':'Kevin'}
set1.update(mydict)
print(set1) #{1, 2, 3, 'dad', 'a', 'b', 'c', 'mom', 't1', 't2'}
# add values of dict to set1 by default
set1.update(mydict.values())
print(set1) 
#{'Sophie', 1, 2, 3, 'dad', 'a', 'b', 'c', 'mom', 't1', 't2', 'Kevin'} 

