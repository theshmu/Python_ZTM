from random import randint
import sys

# generate a number 1~10
def guess_check(guess, answer):
    try:
        if 0 < int(guess) < 11:
            if guess == answer:
                print('you are a genius!')
                return True
        else:
            print('hey bozo, I said 1~10')
            return False
    except ValueError:
        print('Enter a number')
        return False


# input from user?
# check that input is a number 1~10
if __name__ == '__main__':
    answer = randint(1, 10)
    while True:
        try:
            guess = int(input('guess a number 1~10:  '))
            result = guess_check(guess, answer)
            if result:
                break
        except ValueError:
            print('please enter a number')
            continue

