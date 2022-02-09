from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
my_cap_pets = list(map(lambda pet: pet.capitalize(), my_pets))
print(my_cap_pets)

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
zipped = list(zip(my_strings, sorted(my_numbers)))
print(zipped)

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
passed = list(filter(lambda x: bool(x // 50), scores))
print(passed)

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
all_numbers = my_numbers.copy()
all_numbers.extend(scores)

total = reduce(lambda a, b: a + b, all_numbers)
print(total)
print(sum(scores) + sum(my_numbers))
