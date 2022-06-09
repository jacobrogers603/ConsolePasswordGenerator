# Jacob Rogers
# A program to randomly generate a password. The user can specify if he wants to include certain types of characters and the desired length.
# June-9th-2022 

import enum
import pyperclip
from random import random

# List of possible chars to put in the password, a 2D array that is organized with 
    # digits index 0, lower case chars in index 1, upper case chars in index 2, and special character list in in index 3 (32).
charList = [['0','1','2','3','4','5','6','7','8','9'],
['a','b','c','d','e','f','g','h','i','j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '\\', '|', ':', ';', '\'', '\"', '<', '>', ',', '.', '?', '/', '`', '~']]

# Use an IntEnum class to make these labels equivlent to their respective numbers.
class charType(enum.IntEnum):
    digits = 0
    lower_case = 1
    upper_case = 2
    specials = 3

password = ''

promisedSpecialIndex, promisedDigitIndex, promisedUpIndex, passwordLength, curr = -1, -1, -1, 0, 0

# Lower-case characters are always allowed in a password.
allowedLists = [charType.lower_case]

print('----------------------------------------------Random Password Generator---------------------------------------------\n')

# Get the length, require a minimum length of four characters to allow for each type of character.
while passwordLength < 4:
    passwordLength = input('Enter password length: ')

    if passwordLength.isnumeric() == False:
        print('\nPlease enter a positive integer.\n')
        passwordLength = 0
        continue
    
    passwordLength = int(passwordLength)

    if passwordLength < 4:
        print('\nPasswords need to have at least four characters.\n')


# Ask the user if he wants to include certain types of characters in his password.
# If he does, randomly generate a random location in the password where we guantee that that location will have that type of chatracter.
# We also ensure these will not be at the same locations as other guaranteed characters.
print('\n-----------------------------------------------------Directions-----------------------------------------------------\n')
print('You will be prompted to decide the types of characters that will be included in your password.\n')
print('If you want to include something or answer with "yes," type \"1\". Otherwise press any other key.\n')
print('Passwords will always have the chance to contain lower-case characters.\n')
print('A "Standard Password" has lower-case characters, upper-case characters, and digits,\nbut no special characters, (this allows for easy two-click highlighting for convenient copying & pasting).\n')
print('-------------------------------------------------Configure Password-------------------------------------------------\n')

# Standard password selection.
if input('Standard Password: ') == '1':
    promisedDigitIndex = int(random() * 100) % (passwordLength - 1)
    promisedUpIndex = int(random() * 100) % (passwordLength - 1)
    allowedLists.append(charType.digits)
    allowedLists.append(charType.upper_case)

# User wants to create rules different than the standard password selection.
else:
    if input('Special Characters: ') == '1':
        promisedSpecialIndex = int(random() * 100) % (passwordLength - 1)
        allowedLists.append(charType.specials)

    if input('Digits: ') == '1':
        allowedLists.append(charType.digits)

        while promisedDigitIndex == promisedSpecialIndex or promisedDigitIndex == -1:
            promisedDigitIndex = int(random() * 100) % (passwordLength - 1)

    if input('Uppercase letters: ') == '1':
        allowedLists.append(charType.upper_case)

        while promisedUpIndex == promisedSpecialIndex or promisedUpIndex == promisedDigitIndex or promisedUpIndex == -1:
            promisedUpIndex = int(random() * 100) % (passwordLength - 1)

# Loop to append one letter at a time to the password.
while curr < passwordLength:

    # Check if the password is at a point where we guaranteed that a certain character type would be insterted and if so pull from that list.
    if curr == promisedSpecialIndex:
        listChoice = charType.specials
    elif curr == promisedDigitIndex:
        listChoice = charType.digits
    elif curr == promisedUpIndex:
        listChoice = charType.upper_case
    # Else, choose a random list while not including any lists that were not called for by the user.
    else:
        listChoice = allowedLists[int(random() * 100) % len(allowedLists)]
        
            
    # Choose a random element from the chosen list to append to the password.
    if listChoice == charType.digits:
        indexChoice = int(random() * 100) % 10
    elif listChoice == charType.specials:
        indexChoice = int(random() * 100) % 32
    elif listChoice == charType.lower_case or listChoice == charType.upper_case:
        indexChoice = int(random() * 100) % 26
            
    password += charList[listChoice][indexChoice]
    curr += 1

print('\nPassword:', password)
pyperclip.copy(password)
print('\nThe password has been copied to your clipboard.')