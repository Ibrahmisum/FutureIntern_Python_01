import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess =int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Too Low,Please try again.')
        elif guess > random_number:
            print('Too High, Please try again. ')

    print(f'Congratulations, You have guessed the number {random_number}')

guess(100)