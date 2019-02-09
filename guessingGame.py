# Guessing Game programming practice

import random

guessesTaken = 0

print('\n Hello! What is your name? \n')
myName = input()

number = random.randint(1,999)
print('\n Well, ' + myName + ', I am thinking of a number between 1 and 999.')

while guessesTaken < 10:
    print('\n Take a guess. You have ' + str((10 - guessesTaken)) + ' guesses remaining \n')
    # print(number) # Uncomment to show the computer's number for debugging
    guess = int(input())

    guessesTaken = guessesTaken + 1

    if guess < number:
        print ('\n Your guess is too low.')

    if guess > number:
        print('\n Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('\n Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses! \n')

if guess != number:
    number = str(number)
    print('\n Nope. The number I was thinking of was ' + number + '\n')
