"""
TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and
        print the encrypted text.
TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message
TODO-4: Combine encrypt + decrypt into a single Caesar() function
TODO-5: Caesar should take all 3 user inputs
"""

import os

# TODO-Jake: There has to be a way to make this index wrap right? so i can half the alphabet size
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def askTextShift():  # originally, this was cause i had found it easiest to ask in both the original encrypt / decrypt
                     # ended up being used still to simply the main while loop.
    text = input("Type your message:\n").lower().strip()
    shift = int(input("Type the shift number:\n"))
    return text, shift


def caesar(text, shiftamt, eORd):
    message = ''

    # check if you need which direction you need to move from your starting letter
    if eORd == 'd':
        shiftamt *= -1

    #replace letters as needed
    for letter in text:
        pos = ALPHABET.index(letter)
        new_pos = pos + shiftamt
        message += ALPHABET[new_pos]

    #print message and wait for user to see it, clear screen after
    print(f"Your new message is : {message}")
    input("Waiting...")
    os.system("cls")


while True:
    # Ask user for what they'd like to do
    direction = input("Type 'enc' to encrypt, type 'dec' to decrypt, 'q' to quit:\n")

    # Get user inputs
    result = askTextShift()

    # Run Encrypt/Decrypt
    caesar(result[0], result[1], direction[0])

