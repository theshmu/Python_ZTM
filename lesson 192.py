import re

'''
Password must be al least 8 characters of any letter, number  or @#$% and end with a number
'''
pattern = re.compile(r"^[A-Za-z0-9@#$%]{7,}[0-9]$")

while True:
    password = input('Please enter your password: ')
    valid = pattern.fullmatch(password)
    if valid is None:
        print(
            'Password is invalid, must be 8 characters long with letters, numbers or \'@#$%\' and end with a number')
        continue
    else:
        print(f'password {password} is valid :)')
        break

print(valid)
