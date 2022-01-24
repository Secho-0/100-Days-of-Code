
from art import HIGHLOW,VERSUS
from os import system
import random as r
import highlowdata as hld

# Print Logo
# Get 1 Account
# VS Logo
# Get 2nd Account
# Get Input from user
# check if user is correct 

def get_account(acc_list):
    """ Choose an acccount from within the game data to use for comparison """
    chosen_one =  r.choice(acc_list)
    return chosen_one

def print_account(acc):
    """Print the name and information of an account from the game data"""
    name = acc['name']
    job = acc['description']
    country = acc['country']
    acc_string = (f"{name}, a(n) {job}, from {country}.")
    return acc_string

def compare_accounts(acc1, acc2, uGuess):
    """Compare the User guess and accounts to see which has more followers, and if the User was correct"""

    if acc1['follower_count'] >  acc2['follower_count']:
        return uGuess == 'a'
    if acc1['follower_count'] < acc2['follower_count']:
        return uGuess == 'b'
            

def game():
    finished = False 
    score = 0
    print(HIGHLOW)

    while not finished:
        # Pick two accounts, check that theyre not the same one 
        if score == 0:
            first_acc = get_account(gamedata)
            second_acc = get_account(gamedata)
        else:
            first_acc = second_acc
            second_acc = get_account(gamedata)
        while second_acc == first_acc:
                second_acc = get_account(gamedata)

        # Print the accounts to compare 
        print("Compare 'A': " + print_account(first_acc))
        print(VERSUS)
        print("Against 'B': " + print_account(second_acc))

        #Ask user for their guess 
        guess = input("Who has more followers? 'A' or 'B'? ").lower()

        #End game / Increase score based depending on if user is correct 
        iscorrect = compare_accounts(first_acc,second_acc,guess)
        if iscorrect:
            system("cls")
            print(HIGHLOW)
            score += 1

        else: 
            print("Game Over :(")
            print(f"\t You scored: {score}")
            finished = True

gamedata = hld.data

game()