#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
player1 = {
    'age': input('What is your age? '),
    'username': input('What is your username? '),
    'weapons': 'Hunting Knife',
    'is_active': True,
    'clan': 'Team blue'

}
#2 iterate and print all the keys in the above user.
print(player1)
#3 Add a new weapon to your user
player1.update({'weapons': 'sword'})
print(player1)
#4 Add a new key to include 'is_banned'. Set it to false
player1.update({'is_banned': False})
print(player1)

#5 Ban the user by setting the previous key to True
player1.update({'is_banned': True})
print(player1)
#6 create a new user2 my copying the previous user and update the age value and username value.
player2 = player1.copy()
player2.update({'age': input('What is your age? ')})
player2.update({'username': input('What is your username? ')})
print(player1)
print(player2)