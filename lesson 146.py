# Square
my_list = [9, 8, 5, 3, 101]
print(list(map(lambda x: x ** 2, my_list)))

# List sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)
