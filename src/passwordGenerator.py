# Jacob Rogers
# A program to randomly generate a password. The user can specify if he wants to include certain types of characters and the desired length.
# June-9th-2022 

import enum
from operator import index
import pyperclip
from random import random
from random import choice

# List of possible chars to put in the password, a 2D array that is organized with 
# digits index 0, lower case chars in index 1, upper case chars in index 2, and special character list in in index 3 (32).
charList = [['0','1','2','3','4','5','6','7','8','9'],
['a','b','c','d','e','f','g','h','i','j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '\\', '|', ':', ';', '\'', '\"', '<', '>', ',', '.', '?', '/', '`', '~']]

runProgram = '1'
debug = False

while runProgram == '1':

    password = ''
    promisedLowIndex, promisedSpecialIndex, promisedDigitIndex, promisedUpIndex, passwordLength, curr = -1, -1, -1, -1, 0, 0
    allowedLists = []

    # Use an IntEnum class to make these labels equivlent to their respective numbers.
    class charType(enum.IntEnum):
        digits = 0
        lower_case = 1
        upper_case = 2
        specials = 3

    print('\n----------------------------------------------Random Password Generator---------------------------------------------\n')

    # Get the length, require a minimum length of four characters to allow for each type of character.
    while passwordLength < 4:
        passwordLength = input('Enter password length: ')

        if passwordLength.isnumeric() == False:
            # Debug mode.
            if passwordLength == 'debug':
                if debug:
                    debug = False
                    print('Debug mode off.')
                else:
                    debug = True
                    print('Debug mode on.')

            print('\nPlease enter a positive integer.\n')
            passwordLength = 0
            continue
        
        passwordLength = int(passwordLength)

        if passwordLength < 4:
            print('\nPasswords need to have at least four characters.\n')


    # Ask the user if he wants to include certain types of characters in his password.
    # If he does, randomly generate a location in the password where we guantee that location will have that type of chatracter.
    # We also ensure these will not be at the same locations as other guaranteed characters.
    print('\n-----------------------------------------------------Directions-----------------------------------------------------\n')
    print('You will be prompted to decide the types of characters that will be included in your password.\n')
    print('If you want to include something or answer with "yes," type \"1\". Otherwise press any other key.\n')
    print('A "Standard Password" has lower-case characters, upper-case characters, and digits,\nbut no special characters, (this allows for easy two-click highlighting for convenient copying & pasting).\n')
    print('-------------------------------------------------Configure Password-------------------------------------------------\n')

    while allowedLists == []:
        # Standard password selection.
        if input('Standard Password: ') == '1':
            promisedDigitIndex = choice(list(range(passwordLength)))
            promisedUpIndex = choice([i for i in range(passwordLength) if i != promisedDigitIndex])
            promisedLowIndex = choice([i for i in range(passwordLength) if (i != promisedDigitIndex and i != promisedUpIndex)])

            allowedLists.append(charType.digits)
            allowedLists.append(charType.lower_case)
            allowedLists.append(charType.upper_case)

        # User wants to create rules different than the standard password selection.
        else:
            if input('Lowercase letters: ') == '1':
                promisedLowIndex = choice(list(range(passwordLength)))
                allowedLists.append(charType.lower_case)

            if input('Special characters: ') == '1':
                promisedSpecialIndex = choice([i for i in range(passwordLength) if i != promisedLowIndex])
                allowedLists.append(charType.specials)

            if input('Digits: ') == '1':
                promisedDigitIndex = choice([i for i in range(passwordLength) if (i != promisedLowIndex and i != promisedSpecialIndex)])
                allowedLists.append(charType.digits)

            if input('Uppercase letters: ') == '1':
                promisedUpIndex = choice([i for i in range(passwordLength) if (i != promisedLowIndex and i != promisedSpecialIndex and i != promisedDigitIndex)])
                allowedLists.append(charType.upper_case)

        if allowedLists == []:
            print('You must choose at least one type of character to be allowed in your password.\n')

        if debug: 
                print('\n\npromisedDigitIndex =', promisedDigitIndex, 'promisedLowIndex =', promisedLowIndex, 
                '\npromisedUpIndex =', promisedUpIndex, 'promisedSpecialIndex =', promisedSpecialIndex, '\nallowedLists = ', allowedLists,'\n\n')


    # Loop to append one letter at a time to the password.
    while curr < passwordLength:

        # Check if the password is at a point where we guaranteed that a certain character type would be insterted and if so pull from that list.
        if curr == promisedLowIndex:
            listChoice = charType.lower_case
        elif curr == promisedSpecialIndex:
            listChoice = charType.specials
        elif curr == promisedDigitIndex:
            listChoice = charType.digits
        elif curr == promisedUpIndex:
            listChoice = charType.upper_case
        # Else, choose a random list while not including any lists that were not called for by the user.
        else:
            listChoice = choice(allowedLists)
                
        # Choose a random element from the chosen list to append to the password.
        if listChoice == charType.digits:
            indexChoice = int(random() * 100) % 10
        elif listChoice == charType.specials:
            indexChoice = int(random() * 100) % 32
        elif listChoice == charType.lower_case or listChoice == charType.upper_case:
            indexChoice = int(random() * 100) % 26

        if debug: 
            print('\ncurr = ', curr, '\nlistChoice = ', listChoice, ' indexChoice = ', indexChoice, 
            '\ncharList[',listChoice,']','[',indexChoice,']','\n--------------------------------------', sep='')
                
        password += charList[listChoice][indexChoice]
        curr += 1

    print('\nPassword:', password)
    pyperclip.copy(password)
    print('\nThe password has been copied to your clipboard.')

    runProgram = input('\nPress "1" to generate another password, or press any other key to quit: ')


