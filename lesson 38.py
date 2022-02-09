from datetime import date

birth_year = int(input('What year were you born in? '))
current_year = date.today()
age = int(current_year.year - birth_year)

print(f'You are between {age-1} and {age} years old!')
