import sys
import random

low = int(sys.argv[1])
high = int(sys.argv[2])
rng_num = random.randint(low, high)

counter = 1
while True:
    guess = input('Please enter your guess, or type \'x\' to give up: ')
    try:
        if guess == 'x':
            print(f'You have given up after {counter} tries :( the correct number was {rng_num}')
            break

        elif int(guess) == rng_num:
            print(f'Congratulations! you are correct!! it took you {counter} tries')
            break
        else:
            print('Incorrect, please try again')
            counter += 1
    except TypeError:
        print('Please enter a number or \'x\': ')
    except ValueError:
        print('Only enter a number or \'x\'. ')
