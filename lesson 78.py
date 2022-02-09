# Exercise: Check for duplicates in list

my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates_list = []

for item in my_list:
    if my_list.count(item) > 1 and duplicates_list.count(item) == 0:
        duplicates_list.append(item)

print(f'The duplicate values are {duplicates_list}')
