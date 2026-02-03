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