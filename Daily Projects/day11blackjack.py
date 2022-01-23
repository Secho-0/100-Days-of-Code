'''############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.'''

'''############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.'''

import random as r
import art
def dealCard():
    """Return a random card from the deck"""
    deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return r.choice(deck)

def scoreHand(hand):
    """Total the score in each hand"""
    score = sum(hand)

    # Check for Blackjack
    if score == 21 and len(hand) == 2:
        score = 0
        return score 
    
    #Make Ace low
    if 11 in hand and score > 21:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)
    return score
    
def compareHands(playerscore,computerscore):
    """Compare both player and computer hands to determine winner"""
    if playerscore > 21 and computerscore > 21:
        return "You went over. You lose 😤"

    if playerscore == computerscore:
        return "Draw 🙃"
    elif computerscore == 0:
        return "Lose, opponent has Blackjack 😱"
    elif playerscore == 0:
        return "Win with a Blackjack 😎"
    elif playerscore > 21:
        return "You went over. You lose 😭"
    elif computerscore > 21:
        return "Opponent went over. You win 😁"
    elif playerscore > computerscore:
        return "You win 😃"
    else:
        return "You lose 😤"

def blackjack():
    print(art.BLACKJACK)

    player_cards = []
    computer_cards = []
    user_turn = True
    
    # Deal cards to player and computer 
    for i in range(2):
        player_cards.append(dealCard())
        computer_cards.append(dealCard())

    # Have player take their turn, ask for Hit or Pass - no Fold
    while user_turn:
        player_score = scoreHand(player_cards)
        computer_score = scoreHand(computer_cards)
        print(f"You currently have a hand of {player_cards} with a score of {player_score}")
        print(f"The Computer's first cards is {computer_cards[0]}")

        if player_score == 0 or player_score > 21 or computer_cards == 0:
            playing = False
        else:
            askdeal = input("Would you like to (H)it or (P)ass?> ").lower()
            if askdeal.startswith('h'):
                player_cards.append(dealCard())
            else:
                user_turn = False

    # Computer takes turns until >= 17 
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(dealCard())
        computer_score = scoreHand(computer_cards)

    # compare and print final hands
    print(compareHands(player_score,computer_score))
    print(f"Your final score was{player_score}, with a hand of {player_cards}")
    print(f"The computer finals score was {computer_score}, with a hand of {computer_score}")

#Ask for new game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    blackjack()
