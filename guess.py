##### GUESSING GAME ##################
#### Made by Nick Clark ##############

import random

# Range of number

lonum, hinum = 1, 20
theMagicNumber = int(random.randint(lonum, hinum))

# To Keep track of your guesses
guessesTaken = 0

myName = raw_input('Hello! What is your name? ')

print('Well ' + myName + '!  I am thinking of a number between ' + str(lonum) + ' and ' + str(hinum) +  '.')
print('You have 6 chances to guess my number.  Good Luck!!!')
print("\n")

# Begin While loop to check on guess
while guessesTaken < 6:
    
    myGuess = int(raw_input('\033[0;37;40m Take a guess! '))
    print("\n")
    guessesTaken = guessesTaken + 1

    if myGuess < theMagicNumber:
        print('\033[1;31;40m Your guess is too low.') # There are eight spaces in front of print.
        print("\n")
        print('You now have ' + str(6 - guessesTaken) + ' left to guess')
        print("\n")

    if myGuess > theMagicNumber:
        print('\033[1;34;40m Your guess is too high.')
        print("\n")
        print('You now have ' + str(6 - guessesTaken) + ' left to guess')
        print("\n")

    if myGuess == theMagicNumber:
        break

if myGuess == theMagicNumber:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if myGuess != theMagicNumber:
    print('\033[1;35;40m Nope. The number I was thinking of was ' + str(theMagicNumber))

