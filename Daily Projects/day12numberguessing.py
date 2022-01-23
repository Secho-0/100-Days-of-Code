#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import os 
import random as r
from art import NUMBERGUESS as logo


def compare(userGuess,compNum):
    """Compare the Users guess and the computers number"""

    if userGuess == compNum:
        print(f"You guessed the number! Congrats.\n the number was {compNum}")
        return True
    elif userGuess > compNum:
        print("Too high. Kinda like me most days ")
        return False
    elif userGuess < compNum:
        print("Too Low. Also like me, but my emotional state")
        return False 

def play(compNum, diff):
    """PlaytheGame"""
    winner = False
    #set number of guesses allowed 
    if diff == 'easy':
        ct = 10
    elif diff == 'hard':
        ct = 5

    #okay lets start guessing
    while not winner:
        print(f"You have {ct} guess(es) remaining, good luck.")
        userGuess = int(input("What number you thinkin'? "))
        if compare(userGuess, compNum):
            print("Fucking mindreader eh?")
            winner = True
        ct -= 1 
        if ct == 0:
            print(f"Sorry you lose :(\n the number was {compNum}")
        input("...Press <enter>...")
        os.system("cls")
        print(logo)

finished = False
while not finished:

    # Print logo, generate a number 
    print(logo)
    mysteryNum = r.randint(1,100)
    print("I got a number in mind between 1 and 100... What is it?")
    
    #difficulty check 
    userDiff= input("Would you like to play 'easy' or 'hard'?\n> ").lower()
    
    #play the game 
    play(mysteryNum,userDiff)

    #check if they want to play again 
    play_again = input("Would you like to play again? (Y)es or (N)o").lower()
    if not play_again.startswith('y') or play_again.startswith('n'):
        print("Invalid choice.")
        print(play_again)
    if play_again.startswith('y'):
        continue
    elif play_again.startswith('n'):
        finished = False
        



