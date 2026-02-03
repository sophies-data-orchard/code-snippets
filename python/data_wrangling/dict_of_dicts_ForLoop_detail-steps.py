# Dictionary of dictionaries

students = {
    "Alice": {
        "school": "Greenwood High",
        "grade": "10th"
    },
    "Bob": {
        "school": "Lakeside Middle",
        "grade": "8th"
    },
    "Charlie": {
        "school": "Hilltop Elementary",
        "grade": "5th"
    }
}
students.keys()
# dict_keys(['Alice', 'Bob', 'Charlie'])
students.values()
# dict_values([{'school': 'Greenwood High', 'grade': '10th'}, {'school': 'Lakeside Middle', 'grade': '8th'}, {'school': 'Hilltop Elementary', 'grade': '5th'}])
type(students['Alice'])
# <class 'dict'>
type(students['Alice'].values())
# <class 'dict_values'>

name_set = set()
school_set = set() 
grade_set = set()
for name in students:
    # print(name)
        # Alice
        # Bob
        # Charlie
    # name_set.add(name)
    for school in name:
        print(school)
                A
                l
                i
                c
                e
                B
                b
                C
                h
                a
                r
                l
                i
                e

# The issue is that in the inner loop, you’re iterating over 
# the characters of the string name instead of accessing the 
# nested dictionary. To access the school names, you need to 
# iterate over the dictionary values correctly.
for name in students:
    # print(name)
        # Alice
        # Bob
        # Charlie
    # name_set.add(name)
    # print(students[name]['school'])
        # Greenwood High
        # Lakeside Middle
        # Hilltop Elementary
    # school_set.add(students[name]['school'])
    # print(students[name]['grade'])
            # 10th
            # 8th
            # 5th
    grade_set.add(students[name]['grade'])

print(grade_set)
# {'5th', '10th', '8th'}
print(school_set)
# {'Greenwood High', 'Lakeside Middle', 'Hilltop Elementary'}

print(name_set)
# {'Bob', 'Alice', 'Charlie'}

# 3 levels of nested dicts

university = {
    "Engineering": {
        "Computer Science": {
            "students": ["Alice", "Bob", "Charlie"],
            "courses": ["Algorithms", "Data Structures", "Machine Learning"]
        },
        "Electrical Engineering": {
            "students": ["David", "Eva", "Frank"],
            "courses": ["Circuits", "Electromagnetics", "Signal Processing"]
        }
    },
    "Arts": {
        "History": {
            "students": ["Grace", "Hannah", "Ian"],
            "courses": ["Ancient History", "Modern History", "Art History"]
        },
        "Literature": {
            "students": ["Jack", "Karen", "Leo"],
            "courses": ["Poetry", "Novels", "Drama"]
        }
    }
}

nested_data = {
  "first_name": "John",
  "last_name": "Smith",

    "address": {
    "street_address": "21 2nd Street",
    "city": "New York",
    "state": "NY",
    "postal_code": "10021-3100"},
}

type(nested_data)
# <class 'dict'>

for key, value in nested_data.items():
    print(f'key:"{key}\nvalue:{value}')

for k, v in nested_data.items():
    print(f'This is key:{k}, and this is the value {v}')

len(nested_data)
# 3
type(nested_data['address'])
# <class 'dict'>
print(type(nested_data["last_name"]))
# <class 'str'>
# >>>

print(type(nested_data['first_name']))
# <class 'str'>
for k,v in nested_data['address'].items():
    print(f'key:{k}, value:{v}')

for k, v in nested_data['address'].items():
    print(f'subkey:{k} subval:{v}')
nested_data['address']['city']
nested_data['address']['postal_code']
nested_data['first_name']
nested_data['last_name']

dict_of_lists = {
    "names":["Rich","Chris","Katie"],
    "cities":["Atlanta","Los Angeles",["Chattanooga","Nashville"]]
}

print(dict_of_lists['cities'][2][1])
# Nashville
print(dict_of_lists['names'][2])
# Katie

list_of_dicts = [
    {"names":"Rich",
     "cities":"Atlanta"},
    {"names":"Chris",
     "cities":"Los Angeles"},
    {"names":"Katie",
     "cities":["Chattanooga","Nashville"]},
]

city_set = set()
name_set = set()

for dict in list_of_dicts:
    # print(dict['names'])
    # print(dict['cities'])
    name_set.add(dict['names'])
    # if type(dict['cities'])!=list:  #list not 'list'
    if type(dict['cities'])is not list:  #list not 'list'
        # print(dict['cities'])   #Atlanta Los Angeles
        city_set.add(dict['cities'])
    else:
        for list_item in dict['cities']:
            # print(list_item) #Chattanooga Nashville
            city_set.add(list_item)
print(name_set) 
#{'Katie', 'Chris', 'Rich'}
print(city_set)  
#{'Atlanta', 'Los Angeles', 'Chattanooga', 'Nashville'}


# For loop
# Hypothetical Exam Question
# Given a list of dictionaries, return 2 sets: set of unique cities and set of unique names.

# dict_of_lists = {
#     "names":["Rich","Chris","Katie"],
#     "cities":["Atlanta","Los Angeles",["Chattanooga","Nashville"]]
# } <--- try this later ************

list_of_dicts = [
    {"names":"Rich",
     "cities":"Atlanta"},
    {"names":"Chris",
     "cities":"Los Angeles"},
    {"names":"Katie",
     "cities":["Chattanooga","Nashville"]},
]

# step 1: check the data type: use python tutor
            # type()
type(list_of_dicts)
# <class 'list'>
type(list_of_dicts[0])
type(list_of_dicts[1])
type(list_of_dicts[2])
# <class 'dict'>
# <class 'dict'>
# <class 'dict'>
type(list_of_dicts[0]['names'])
# <class 'str'>
type(list_of_dicts[1]['cities'])
# <class 'str'>
type(list_of_dicts[2]['cities'])
# <class 'list'>

# step2: initialize 2 sets
# set gives unique value
names_set = set()
cities_set = set()
# b/c it's a list of dict, iterate the list
for dict in list_of_dicts:
    # 1.check the keys of the dict
    # print(dict) # check the items of list 
        # {'names': 'Rich', 'cities': 'Atlanta'}
        # {'names': 'Chris', 'cities': 'Los Angeles'}
        # {'names': 'Katie', 'cities': ['Chattanooga', 'Nashville']}
    # 2.Check key 'names'
    # print(dict['names'])
        # Rich
        # Chris
        # Katie
    # key 'names' are clean, get the names 
    # directly and add to set, then print it to see the result
    names_set.add(dict['names'])
    # 3. check 'cities'
    # print(dict['cities'])
        # Atlanta
        # Los Angeles
        # ['Chattanooga', 'Nashville']
    # cities has strings and list, need if...else
    # 1st, deal with string and add to set 
    # 2nd, iterate the list, then add to set
    if type(dict['cities']) is str: #<- don't forget the type(), otherwise no value will be pass to set
        cities_set.add(dict['cities'])
    else:
        # iterate the list of cities
        for nested_city in dict['cities']:
                # to test the logic of above line
                # print(item)
                    # Chattanooga
                    # Nashville
                # proved above logic is good, then add to set
                cities_set.add(nested_city)   #<- at this point, all the info is added to the sets
    

print(cities_set)
# # at if step:
# {'Atlanta', 'Los Angeles'}
# at else step:'Chattanooga', 'Nashville' are added to the set
# {'Atlanta', 'Los Angeles', 'Chattanooga', 'Nashville'}

print(names_set)
# {'Katie', 'Chris', 'Rich'}


# Create 2 sets for names and cities
# dict of lists

dict_of_lists = {
    "names":["Rich","Chris","Katie"],
    "cities":["Atlanta","Los Angeles",["Chattanooga","Nashville"]]
}

# 1. type() and python Tutor
type(dict_of_lists)
# <class 'dict'>
type(dict_of_lists['names'])
type(dict_of_lists['names'][0])
type(dict_of_lists['names'][1])
type(dict_of_lists['names'][2])
# >>> type(dict_of_lists['names'])
# <class 'list'>
# >>> type(dict_of_lists['names'][0])
# <class 'str'>
# >>> type(dict_of_lists['names'][1])
# <class 'str'>
# >>> type(dict_of_lists['names'][2])
# <class 'str'>

# <class 'list'>
type(dict_of_lists['cities'])
# <class 'list'>
type(dict_of_lists['cities'][0])
type(dict_of_lists['cities'][1])
type(dict_of_lists['cities'][2])

# >>> type(dict_of_lists['cities'][0])
# <class 'str'>
# >>> type(dict_of_lists['cities'][1])
# <class 'str'>
# >>> type(dict_of_lists['cities'][2])
# <class 'list'> <-------DDD



print(dict_of_lists.values())
# dict_values([['Rich', 'Chris', 'Katie'], ['Atlanta', 'Los Angeles', ['Chattanooga', 'Nashville']]])
print(dict_of_lists.keys())
# dict_keys(['names', 'cities'])
print(dict_of_lists.items())
# dict_items([('names', ['Rich', 'Chris', 'Katie']), ('cities', ['Atlanta', 'Los Angeles', ['Chattanooga', 'Nashville']])])
for k,v in dict_of_lists.items():
    print(f'keys:{k}\nvalues:{v}')
# keys:names
# values:['Rich', 'Chris', 'Katie']
# keys:cities
# values:['Atlanta', 'Los Angeles', ['Chattanooga', 'Nashville']]

names_set2 = set()
cities_set2 = set()
# for k,v in dict_of_lists.items():
#     # print(v)
#         # ['Rich', 'Chris', 'Katie']
#         # ['Atlanta', 'Los Angeles', ['Chattanooga', 'Nashville']]
#     # print(k)
#         # names
#         # cities
for city in dict_of_lists['cities']:
    # print(city)
    #     Atlanta
    #     Los Angeles
    #     ['Chattanooga', 'Nashville']
    if type(city) is str:
        cities_set2.add(city)
    else:
        for nested_city in city:
            cities_set2.add(nested_city)

print(cities_set2)
# {'Atlanta', 'Los Angeles'} -if
# {'Atlanta', 'Los Angeles', 'Chattanooga', 'Nashville'} -else

for name in dict_of_lists['names']:
    if type(name) is str:
        names_set2.add(name)
    else:
        for nested_name in name:
            names_set2.add(nested_name)

print(names_set2)
# {'Katie', 'Chris', 'Rich'}

# list of tuples
list_of_tuples = [
    ("Rich","Atlanta"),
    ("Chris","Los Angeles"),
    ("Katie",["Chattanooga","Nashville"])
]

type(list_of_tuples)
# <class 'list'>
type(list_of_tuples[0])
type(list_of_tuples[1])
type(list_of_tuples[2])
type(list_of_tuples[2][0])
type(list_of_tuples[2][1])
# >>> type(list_of_tuples[1])
# <class 'tuple'>
# >>> type(list_of_tuples[2])
# <class 'tuple'>
# >>> type(list_of_tuples[2][0])
# <class 'str'>
# >>> type(list_of_tuples[2][1])
# <class 'list'>
len(list_of_tuples)
# 3
len(list_of_tuples[2])
# 2

cities_set3 = set()
names_set3 = set()

# check the details of the tuple in for loop
# for tuple in list_of_tuples:
    # print(tuple)
    # ('Rich', 'Atlanta')
    # ('Chris', 'Los Angeles')
    # ('Katie', ['Chattanooga', 'Nashville'])
    # print(tuple[0])
        # Rich
        # Chris
        # Katie
    # print(tuple[1])
    #     Atlanta
    #     Los Angeles
    #     ['Chattanooga', 'Nashville']
    # print(tuple[2])
    #     Traceback (most recent call last):
    #     File "<stdin>", line 14, in <module>
    #     IndexError: tuple index out of range

for tuple in list_of_tuples:
    names_set3.add(tuple[0])
    if type(tuple[1]) is str:
        cities_set3.add(tuple[1])
    else:
        for nested_city in tuple[1]:
            cities_set3.add(nested_city)


print(cities_set3)
# {'Atlanta', 'Los Angeles'} #<-if
# {'Atlanta', 'Los Angeles', 'Chattanooga', 'Nashville'} #<- else

print(names_set3)
# {'Katie', 'Chris', 'Rich'}


list_of_lists = [
    ["Rich","Chris","Katie"],
    ["Atlanta","Los Angeles",["Chattanooga","Nashville"]]
]

type(list_of_lists)
# list_of_lists
len(list_of_lists)
# 2
type(list_of_lists[0])
type(list_of_lists[1])
type(list_of_lists[1][0])
type(list_of_lists[1][1])
type(list_of_lists[1][2])

# >>> type(list_of_lists[0])
# >>> type(list_of_lists[1])
# <class 'list'>
# >>> type(list_of_lists[1][0])
# <class 'str'>
# >>> type(list_of_lists[1][1])
# <class 'str'>
# >>> type(list_of_lists[1][2])
# <class 'list'>
# >>>

# create 2 lists
city_list = []
name_list = []

for i in list_of_lists:
    # print(i)
        # ['Rich', 'Chris', 'Katie']
        # ['Atlanta', 'Los Angeles', ['Chattanooga', 'Nashville']]
    for nested_i in list_of_lists[0]:
        print(nested_i)
        # Rich
        # Chris
        # Katie
        # Rich
        # Chris
        # Katie
    
# The reason your code prints the names multiple times is because of the way the nested loops are structured. Specifically, the inner loop is always iterating over list_of_lists[0], which contains the names, for each element in the outer loop.

# Here’s a breakdown of what’s happening:

# The outer loop iterates over each sublist in list_of_lists.
# For each iteration of the outer loop, the inner loop iterates over list_of_lists[0], which contains the names.
# This results in the names being printed once for each sublist in list_of_lists.

# Corrected Code
# If you want to print each element in list_of_lists, you should adjust the inner loop to iterate over the current sublist (i) instead of always iterating over list_of_lists[0]:


# for i in range(len(list_of_lists)):    
#     print(list_of_lists[i])
# ['Rich', 'Chris', 'Katie']
# ['Atlanta', 'Los Angeles', ['Chattanooga', 'Nashville']]

# Then I should not nested the 2 loops:--->

for name in list_of_lists[0]:
    name_list.append(name)
print(name_list)
# ['Rich', 'Chris', 'Katie']

for city in list_of_lists[1]:
    if type(city) is str:
        city_list.append(city)
    else: 
        for nested_city in city:
            city_list.append(nested_city)

print(city_list)
# ['Atlanta', 'Los Angeles', 'Chattanooga', 'Nashville']


nested_data = {
  "first_name": "John",
  "last_name": "Smith",

    "address": {
    "street_address": "21 2nd Street",
    "city": "New York",
    "state": "NY",
    "postal_code": "10021-3100"},
}
type(nested_data)
# <class 'dict'>
len(nested_data)
# 3
print(nested_data.keys())
# dict_keys(['first_name', 'last_name', 'address'])
print(nested_data.values())
# dict_values(['John', 'Smith', {'street_address': '21 2nd Street', 'city': 'New York', 'state': 'NY', 'postal_code': '10021-3100'}])

print(nested_data.items())

# >>> print(nested_data.items())
# dict_items([('first_name', 'John'), ('last_name', 'Smith'), ('address', {'street_address': '21 2nd Street', 'city': 'New York', 'state': 'NY', 'postal_code': '10021-3100'})])
# >>>
for k,v in nested_data.items():
    print(f'keys:{k}\nvalues:{v}')
# keys:first_name
# values:John
# keys:last_name
# values:Smith
# keys:address
# values:{'street_address': '21 2nd Street', 'city': 'New York', 'state': 'NY', 'postal_code': '10021-3100'}

students = {
    "Alice": {
        "school": "Greenwood High",
        "grade": "10th"
    },
    "Bob": {
        "school": "Lakeside Middle",
        "grade": "8th"
    },
    "Charlie": {
        "school": "Hilltop Elementary",
        "grade": "5th"
    }
}
students.keys()
# dict_keys(['Alice', 'Bob', 'Charlie'])
students.values()
# dict_values([{'school': 'Greenwood High', 'grade': '10th'}, {'school': 'Lakeside Middle', 'grade': '8th'}, {'school': 'Hilltop Elementary', 'grade': '5th'}])
type(students['Alice'])
# <class 'dict'>
type(students['Alice'].values())
# <class 'dict_values'>

name_set = set()
school_set = set() 
grade_set = set()
for name in students:
    # print(name)
        # Alice
        # Bob
        # Charlie
    # name_set.add(name)
    for school in name:
        print(school)
                A
                l
                i
                c
                e
                B
                b
                C
                h
                a
                r
                l
                i
                e

# The issue is that in the inner loop, you’re iterating over 
# the characters of the string name instead of accessing the 
# nested dictionary. To access the school names, you need to 
# iterate over the dictionary values correctly.
for name in students:
    # print(name)
        # Alice
        # Bob
        # Charlie
    # name_set.add(name)
    # print(students[name]['school'])
        # Greenwood High
        # Lakeside Middle
        # Hilltop Elementary
    # school_set.add(students[name]['school'])
    # print(students[name]['grade'])
            # 10th
            # 8th
            # 5th
    grade_set.add(students[name]['grade'])

print(grade_set)
# {'5th', '10th', '8th'}
print(school_set)
# {'Greenwood High', 'Lakeside Middle', 'Hilltop Elementary'}

print(name_set)
# {'Bob', 'Alice', 'Charlie'}

# 3 layers of nested dict
university = {
    "Engineering": {
        "Computer Science": {
            "students": ["Alice", "Bob", "Charlie"],
            "courses": ["Algorithms", "Data Structures", "Machine Learning"]
        },
        "Electrical Engineering": {
            "students": ["David", "Eva", "Frank"],
            "courses": ["Circuits", "Electromagnetics", "Signal Processing"]
        }
    },
    "Arts": {
        "History": {
            "students": ["Grace", "Hannah", "Ian"],
            "courses": ["Ancient History", "Modern History", "Art History"]
        },
        "Literature": {
            "students": ["Jack", "Karen", "Leo"],
            "courses": ["Poetry", "Novels", "Drama"]
        }
    }
}
university.keys()
# dict_keys(['Engineering', 'Arts'])
university.values()
# >>> university.values()
# dict_values([{'Computer Science': {'students': ['Alice', 'Bob', 'Charlie'], 'courses': ['Algorithms', 'Data Structures', 'Machine Learning']}, 'Electrical Engineering': {'students': ['David', 'Eva', 'Frank'], 'courses': ['Circuits', 'Electromagnetics', 'Signal Processing']}}, {'History': {'students': ['Grace', 'Hannah', 'Ian'], 'courses': ['Ancient History', 'Modern History', 'Art History']}, 'Literature': {'students': ['Jack', 'Karen', 'Leo'], 'courses': ['Poetry', 'Novels', 'Drama']}}])

# University ->Univ->department-> students
#                          -> course 
# get college list, depts list, students set, course set
# Investigation version
uni_list = []
dept_list = []
stu_set = set()
course_set = set()
# for uni in university:
#     print(uni)
#     # Engineering
#     # Arts
for uni in university:
    # print(uni)
    # Engineering
    # Arts
    uni_list.append(uni)
    # print(university[uni])
    for dept in university[uni]:
        # print(dept)
        # Computer Science
        # Electrical Engineering
        # History
        # Literature
        dept_list.append(dept)
        for stu in university[uni][dept]['students']:
            stu_set.add(stu)
            # print(stu)
                    # Alice
                    # Bob
                    # Charlie
                    # David
                    # Eva
                    # Frank
                    # Grace
                    # Hannah
                    # Ian
                    # Jack
                    # Karen
                    # Leo
            



print(stu_set)


print(dept_list)
# ['Computer Science', 'Electrical Engineering', 'History', 'Literature']

print(uni_list)
# ['Engineering', 'Arts']





# Clean version
uni_list = []
dept_list = []
stu_set = set()
course_set = set()

for uni in university:
    uni_list.append(uni)

    for dept in university[uni]:
        dept_list.append(dept)

        for stu in university[uni][dept]['students']:
            stu_set.add(stu)
        for course in university[uni][dept]['courses']:
            course_set.add(course)

print(course_set)
# {'Circuits', 'Data Structures', 'Modern History', 'Drama', 'Ancient History', 'Algorithms', 'Machine Learning', 'Signal Processing', 'Poetry', 'Electromagnetics', 'Art History', 'Novels'}
 
print(stu_set)
# {'Alice', 'Eva', 'Grace', 'Frank', 'Karen', 'Leo', 'Charlie', 'Ian', 'Jack', 'Bob', 'David', 'Hannah'}

print(dept_list)
# ['Computer Science', 'Electrical Engineering', 'History', 'Literature']

print(uni_list)
# ['Engineering', 'Arts']
