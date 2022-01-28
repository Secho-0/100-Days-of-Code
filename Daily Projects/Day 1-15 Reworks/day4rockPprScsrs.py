'''
Rock Paper Scissors
- Computer must be able to randomly choose between each of the choices
- Can determine win loss draw
- Ascii art maybeh

- R < P < S < R
'''

import random as r

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
fuckaround = 0
print("Welcome!~ Lets get started ")


print('''Rock Paper Scissors is a pretty simple game all said in done...
       
                    Rock > Scissors > Paper > Rock 
                            or rather
                        Rock Beats Scissors
                        Scissors Beats Paper
                        Paper Beats Rock''')
while True:
    if fuckaround == 10:
        print("You fucked around too much...\n\t\t\t~Begone Satan~")
        break

    print(''' 
     What would you like to choose? 
    (R)ock
    (P)aper
    (S)cissors
    ''')

    player_choice = input("> ")
    computer_choice = r.randint(0, 2)

    # used to test Scissors > Rock
    # computer_choice = 0


    if not (player_choice.lower().startswith('s') or
            player_choice.lower().startswith('r') or
            player_choice.lower().startswith('p')):
        print("please enter a valid choice...")
        fuckaround += 1
        continue

    elif player_choice.lower().startswith('r'):
        player_choice = 0
    elif player_choice.lower().startswith('p'):
        player_choice = 1
    else:
        player_choice = 2

    plays = [rock, paper, scissors]
    choices = [plays[player_choice], plays[computer_choice]]

    print(f"Player chose:\n {choices[0]}")
    print(f"Computer chose:\n {choices[1]}")

    if computer_choice > player_choice or (computer_choice == 0 and player_choice == 2):
        print("Better luck next time v-v")
    elif computer_choice == player_choice:
        print("Its a draw! x-x")
    else:
        print("You Win Congrats \\0/")

    print("Would you like to play again? (Y)es or (N)o")
    play = input("> ")
    if not (play.lower().startswith('y') or play.lower().startswith('n')):
        print("please enter a valid choice...")
        fuckaround += 1
        play = input("> ")
    elif play.lower().startswith('n'):
        break

