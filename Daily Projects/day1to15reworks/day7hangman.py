"""
Day 7 - Hangman project
TODO  - If the user has entered a letter they've already guessed, print the letter and let them know.
      - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
"""

import random as r
import os

import art
import hangman_words as hWords

word_list = hWords.WORD_LIST

lives = 6
game_on = True

hangmans_word = r.choice(word_list)

prev_guesses = []
board = []


def updateDisplay():

    newdisp = ''
    for i in board:
        newdisp += i
    return newdisp


for l in hangmans_word:
    board += '_'

display = updateDisplay()

print(art.HANGMAN)

while game_on:
    print(display)
    #print("Hint the word is: ", hangmans_word)
    #print("You have ", lives, " lives left.")

    # User guesses a letter , check if its been guessed if not add to previous guesses
    uGuess = input("Guess a letter:  ").lower()
    if uGuess in prev_guesses:
        print("You already guessed this letter")
        continue
    else:
        prev_guesses.append(uGuess)

    if uGuess not in hangmans_word:
        lives -= 1
        if lives > 0:
            print("Sorry that letter isnt in here D:")
        if lives <= 0:
            print("You Lost :*(")
            print("The word was ", hangmans_word)
            game_on = False

    for pos in range(len(hangmans_word)):
        if hangmans_word[pos] == uGuess:
            board[pos] = uGuess
            print("Match~")
            display = updateDisplay()
    print(display)

    if "_" not in board:
        print("You Win!")

    print(art.STAGES[lives])
    print("-" * 30)
    print("Previous Guesses:")
    gString = ''
    for guess in prev_guesses:
        print(gString.join(guess), end=' ')
    print()
    os.system('cls')
