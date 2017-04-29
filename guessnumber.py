
import random
computer_number = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

chances = input('How many guesses would you like? ')

for number_of_guesses in range(1, chances+1):
    guess = int(input('Take a wild guess.\n'))


    if guess < computer_number:
        print('Too low.')
    elif guess > computer_number:
        print('Too high.')
    else:
        break    # This condition is the correct guess!

if guess == computer_number:
    print('Finally! It took you ' + str(number_of_guesses) + ' guesses!')
else:
    print('Hey Sherlock, you should\'ve tried ' + str(computer_number))