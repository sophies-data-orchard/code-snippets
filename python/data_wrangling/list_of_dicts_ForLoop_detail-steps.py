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
