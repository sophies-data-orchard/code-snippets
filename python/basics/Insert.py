# insert()
# list.insert(i, elem)
# Here, elem is inserted to the list at the ith index. All the elements after elem are shifted to the right.

# insert() Parameters
# The insert() method takes two parameters:

# index - the index where the element needs to be inserted
# element - this is the element to be inserted in the list

# Notes:
# If index is 0, the element is inserted at the beginning of the list.
# If index is 3, the index of the inserted element will be 3 (4th element in the list).

# The insert() method doesn't return anything; returns None. It only updates the current list.

#ex1: insert an element to the list
test = [9,8,7]
test.insert(0,100)
print(test)
# output:
# [100, 9, 8, 7]

# ex2: insert a tuple(as an element) to the list
mixedList = [{1,3},[5,7,9]]
#number tuple
numberTuple = (2,4)
#insert a tuple to the list
mixedList.insert(1,numberTuple)
print(mixedList)

# output:
# [{1, 3}, (2, 4), [5, 7, 9]]