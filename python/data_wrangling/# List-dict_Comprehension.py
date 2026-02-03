# List,dict comprehension
l1 =  [(3, 'Zoe'), (2, 'Yvon'), (4, 'Charles'), (1, 'David'), (5, 'Allen'), (6, 'Becky'), (7, 'Charles'), (8, 'Anna')]

r1 = [item for item in l1]
print(r1)
# [(3, 'Zoe'), (2, 'Yvon'), (4, 'Charles'), (1, 'David'), (5, 'Allen'), (6, 'Becky'), (7, 'Charles'), (8, 'Anna')]

# get the 1st item of the tuple
print([item[0] for item in l1])
# [3, 2, 4, 1, 5, 6, 7, 8]

# get the 2nd itemof the tuple
print([item[1] for item in l1 ])
# ['Zoe', 'Yvon', 'Charles', 'David', 'Allen', 'Becky', 'Charles', 'Anna']

# people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill", 5:"Allen",6:"Becky"}

l = ["msa", "cse", "6040"]
for i in l:
    print(i)

# msa
# cse
# 6040

range_list_comp =[x for x in range(10)]
print(range_list_comp)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


a_list = [1, '4', 9, 'a', 0, 4]
cal = [item*item for item in a_list if type(item) ==int ]
print(cal)
# [1, 81, 0, 16]

my_list = [1,2,3,4,5,6,7,8,9,10]
evennumber= [n for n in my_list if n%2==0]
print(evennumber)
# [2, 4, 6, 8, 10]

ee=[n if n%2 == 0 else 100 for n in my_list]
print(ee)
# [100, 2, 100, 4, 100, 6, 100, 8, 100, 10]

colors = ["pink", "white", "blue", "black", "purple"]
colors_upper = [c.upper() for c in colors ]
print(colors_upper)
# ['PINK', 'WHITE', 'BLUE', 'BLACK', 'PURPLE']

# list of names
presidents_usa = ["George Washington", "John Adams","Thomas Jefferson","James Madison","James Monroe","Andrew Jackson"]
ans = [name.split(' ') for name in presidents_usa]
print(ans)
# [['George', 'Washington'], ['John', 'Adams'], ['Thomas', 'Jefferson'], ['James', 'Madison'], ['James', 'Monroe'], ['Andrew', 'Jackson']]

back = [name[1].upper()+','+ name[0] for name in ans]
print(back)
# ['WASHINGTON,George', 'ADAMS,John', 'JEFFERSON,Thomas', 'MADISON,James', 'MONROE,James', 'JACKSON,Andrew'] 

# double loops - comprehension
# 1 0 0
# 0 1 0
# 0 0 1
cols = []
rows = []
for row in range(3):
    for col in range(3):
        if col == row:
            cols.append(1)
        else:
            cols.append(0)
    rows.append(cols)
    cols =[]
rows

i_matrix =[[ 1 if col_idx == row_idx else 0 for col_idx in range(0, 3)] for row_idx in range(0,3)]
print(i_matrix)
# [[1, 0, 0], [0, 1, 0], [0, 0, 1]]


loop_dict = {}
for num in range (1,11):
    loop_dict[num] = num&num

loop_dict
# {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}

ld = {num: num*num for num in range(1,11)}
print(ld)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


persons = [
    {
        'name': 'Vuduc',
        'age': 40,
        'title': 'Data Scientist'
    },
    {
        'name': 'Sokol',
        'age': 45,
        'title': 'Data Engineer'
    },
    {
        'name': 'Wooley',
        'age': 43,
        'title': 'Program Director'
    }
]

dict = {p['name']: p['title'] for p in persons if 'Data' in p['title']}
print(dict)
# {'Vuduc': 'Data Scientist', 'Sokol': 'Data Engineer'}

d2={p['name']:p['age'] for p in persons if p['age']>40 and 'Data' in p['title']}
print(d2)

{'Sokol': 45}


https://pythontutor.com/python-compiler.html#mode=edit

# For val in d.keys():
# For Val in d.values():
# For val in d.items()
# Min(d.values()), max(d.values())

