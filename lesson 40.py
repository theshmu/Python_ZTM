username = input('Please input your username: ')
password = input('Please input your password: ')

pass_length = len(password)
hidden_pass = '*' * pass_length

print(f'{username}, your password {hidden_pass} is {pass_length} characters long.')
