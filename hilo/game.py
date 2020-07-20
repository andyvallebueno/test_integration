from random import random

hidden_number: object = random.randint(1, 100)

selected_number = 0

print('Welcome to the HI - LO game')

while selected_number != hidden_number:
    selected_number = input('Guess a number between 1 & 100: ')

    if selected_number < hidden_number:
        print('Too low!')

    elif selected_number > hidden_number:
        print('Too high!')

    elif selected_number == hidden_number:
        print('Got it: The number is '.format(hidden_number))