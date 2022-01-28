import random as r
import art

def dealCard():
    """Adds a random card to the players hand from within the deck.

    Returns:
        int: random integer from the deck list, representitive of a card
    """
    deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return r.choice(deck)

def scoreHand(hand: list):
    """Adds together all the cards in a hand
     Checks for Blackjack if 21, and returns score of 0
     Also checks for an Ace if over 21, make Aces low

    Args:
        hand (list): Hand with the players cards

    Returns:
        int: sum total of the players cards
    """
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
    
def compareHands(playerscore: int,computerscore: int):
    """Compare the hand of the player, and computer to see who is 
    the winner and who is the loser, or if you both lose 

    Args:
        playerscore (int): current sum of all the cards in the players hand
        computerscore (int): current sum of all the cards in the computers hand 

    Returns:
        string: basic string detailing the situation (win/loss/draw/lackjack) 
    """
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
    """ Main blackjack game, may as well just be main()
    """
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

        if (player_score == 0 or player_score > 21 or computer_cards == 0):
            user_turn = False
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
    print(f"Your final score was {player_score}, with a hand of {player_cards}")
    print(f"The computer finals score was {computer_score}, with a hand of {computer_cards}")

#Ask for new game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    blackjack()
