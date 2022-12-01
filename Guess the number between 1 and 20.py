# this is a number gussing game

import random
name = input("Hello! What is your name?  ")
print('Well, '+ name + ' I am thinking of a number between 1 and 20 make a guess.')

secretNumber = random.randint(1,20)

# DEBUGG LINE print('Debug: Secret number is ' + str(secretNumber))

#guessing the number using a for loop to keep guesses below 7
for guessesTaken in range(1,7):
    print('Take a guess')
    guess = int(input())  #must add the int change function
    if guess < secretNumber:
        print('Your guess is too low!')
    elif guess > secretNumber:
        print('your guess is too high!')
    else:
        break # this condition is for the correct guess!

if guess == secretNumber:
    print('Congrats, you won in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope, The number I was thinking of was ' + str(secretNumber) + '!')