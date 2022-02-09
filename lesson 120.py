#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat_1 = Cat('Mittens',10)
cat_2 = Cat('Fluffy',4)
cat_3 = Cat('Crookshanks',20)



# 2 Create a function that finds the oldest cat
def oldest_cat(*args):
	'''
	This function recieves a number of Cat objects and returns the Cat object with the highest age attribute
	'''
	cats = list(args)
	if len(cats) == 0:
		print('You did not enter any cats')
		return
	oldest = cats[0]
	for cat in cats:
		if cat.age > oldest.age:
			oldest = cat


	return oldest


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2 
print(f'The oldest cat is {oldest_cat(cat_1,cat_2,cat_3).name} who is {oldest_cat(cat_1,cat_2,cat_3).age} years old')

