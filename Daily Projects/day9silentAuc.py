import os, art

print("Lets begin the auction!")
print(art.SILENTAUCTION)

def find_highest(bidding_record):
    highest_bid = 0 
    winner = ''
    for bidder in bidding_record:
        bid = bidding_record[bidder]
        if bid > highest_bid:
            highest_bid = bid
            winner = bidder
    print(f"the winnter is {winner}, with a bid of ${highest_bid}")

auction_bidders = {}

while True:


    name = input("What is your name?")
    bid = int(input("What would you like to bid? $"))

    auction_bidders[name] = bid

    more_ppl = input("Is there another bidder?")

    if not (more_ppl.lower().startswith("y") or more_ppl.lower().startswith("n")):
        print("please enter a valid choice")
        more_ppl = input("Is there another bidder?")
    
    if more_ppl.lower().startswith("y"):
        os.system("cls")
        continue
    
    find_highest(auction_bidders)
    break
