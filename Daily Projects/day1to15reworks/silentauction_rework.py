'''
###### Silent Auction Rework ######
# TODO - Add Rules for the auction 
#       (Bidder #s are used not names, Only highest bid is recorded, 
#        names announced at the end of the auction)
# TODO - Auction Module -> Register(?)
# TODO - Bidder class?
# TODO      - Would make dict nesting less intense maybe?
'''

import os, art

class Auction:

    def __init__(self, numitems:int):
        self.bidders = {}
        self.num_bidders = 0
        self.items = {}
        self.num_items = numitems

    def set_items(self):
        """Set the items names and value
        >>format -> item_name:{"value": <int>,"bid": <int>, "winner": <str>}
        """
        for i in range(self.num_items):
            item_name = input("What is the items you are selling?").lower()
            item_value = int(input("What is the value of the item?"))
            self.items[item_name] = {}
            self.items[item_name]["value"] = item_value
            self.items[item_name]["bid"] = item_value
            self.items[item_name]["winner"] = ''
            
    def get_bidders(self):
        """Assign ID Numbers and get names for each Bidder
        """
        self.num_bidders = int(input("How many people are bidding?"))
        #Assign Bidders a number higher than 0, but to the proper index #
        for i in range(1,self.num_bidders+1):
            self.bidders[i-1] = {}
            self.bidders[i-1]["name"] = input("What is your name?").lower()
            #Clear Screen as to not give away information
            input(f"{self.bidders[i-1]['name'].title()}, you are bidder Number {i}\n\tEnter to Clear Screen...")
            os.system("cls")

    def find_highest(self,item:dict):
        """Find the highest bid on an item for sale

        Args:
            item (dict): Dictionary containing the information for the item for sale
        """
        for bidder in self.bidders:
            # Set simpler variable name 
            bid = self.bidders[bidder]["bid"]
            # If the users bid is over the items highest bid, then set a new highest and take winners name
            if bid > self.items[item]["bid"]:
                self.items[item]["bid"] = bid
                # Get winner name 
                self.items[item]["winner"]= self.bidders[bidder]["name"]

    def run_auction(self):
        """Run the auction itself
        """
            #Start of actual Auction
        print(art.SILENTAUCTION.center(72))
        print("Lets begin the auction!".center(72))
 
            #Run through each item for auction
        for item  in self.items:
            bidding = True
            more_bids = ''
            while bidding:
                # Take a bid from each bidder
                for bidder in self.bidders:
                    # If this is the second round, use the highest bidding price instead of the value of the item
                    if more_bids.startswith('y'):
                        print(f"\nBidding will start at ${self.items[item]['bid']} for this - arguably priceless - {item.title()}")
                        bid = int(input(f"\nBids under ${self.items[item]['bid']} will be considered a pass.\nBidder {bidder+1} what would you like to bid?"))
                        self.bidders[bidder]["bid"] = bid 
                    #if first round, use value of the item 
                    else:
                        print(f"\nBidding will start at ${self.items[item]['value']} for this - arguably priceless - {item.title()}")
                        bid = int(input(f"\nBids under ${self.items[item]['value']} will be considered a pass.\nBidder {bidder+1} what would you like to bid?"))
                        self.bidders[bidder]["bid"] = bid
                    # Clear the screen between bids
                    input("Press <Enter> to clear the screen for the next bidder...")
                    os.system("cls")
                self.find_highest(item)
                # Checkfor more bidding
                more_bids = input("Would anyone else like to bid again? (Y)es or (N)o.\n>>").lower()
                if more_bids.startswith('n'):
                    print(f"the winner is {self.items[item]['winner']}, with a bid of ${self.items[item]['bid']}")
                    bidding = False
        print("Thank you for participating in our auction! We hope to see you again.")
        input("<Enter> to clear screen...")
        os.system("cls")





while True: 
    # Find out how many items are up for auction, and tell us what they are 
    a = Auction(int(input("How many items are for auction?")))
    a.set_items()
    #clear screen to hide items from bidders 
    input("Press <enter> when you are ready to start the auction....")
    os.system("cls")
    # Assign a number to each person, to give anonimity
    a.get_bidders()
    # Bid on the auction, update list with bids
    a.run_auction()

    #Check if there is going to be another auction
    another_auction = input("Is there another auction? (Y)es or (N)o.\n>>").lower()
    if another_auction.startswith('y'):
        continue
    if another_auction.startswith('n'):
        bidding = False
        break
    else:
        print("Invalid Choice.\n",another_auction)



'''#### Original Code - some functions were reused ####
    # name = input("What is your name?")
    # bid = int(input("What would you like to bid? $"))

    # auction_bidders[name] = bid

    # more_ppl = input("Is there another bidder?")

    # if not (more_ppl.lower().startswith("y") or more_ppl.lower().startswith("n")):
    #     print("please enter a valid choice")
    #     more_ppl = input("Is there another bidder?")
    
    # if more_ppl.lower().startswith("y"):
    #     os.system("cls")
    #     continue
    
    # find_highest(auction_bidders)
    # break
'''