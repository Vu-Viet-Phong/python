# This is a guess the number game.
import random

secretsNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20')

# Ask the player to guess 6 times
for guessesTaken in range(1, 5):
    print('Take a guess')
    guess = int(input())

    if guess < secretsNumber:
        print('Your guess too low.')
    elif guess > secretsNumber:
        print('Your guess is too high.')
    else: # This condition is the correct guess!
        break

if guess == secretsNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretsNumber))