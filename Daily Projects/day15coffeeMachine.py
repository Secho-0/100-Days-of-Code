"""
Day 15 Final Project - Make a coffee machine, coin operated, that serves three different drinks, return change, and is aware
if it is short on resources or not
"""

from art import COFFEE as logo

MENU = { "espresso": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
            },
            "cost": 1.5,
    },

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },

    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "cash":0,
}

def report():
    """ Return a report of the available resources 
    Arguments: none
    Return: none, simple print statement
    """
    for resource in resources:
        if resource != "cash" and resource != "coffee":
            print(resource.capitalize() + ":", resources[resource], "ml")
        if resource == "coffee":
            print(resource.capitalize() + ":", resources[resource], "g")
        if resource == "cash":
            print(resource.capitalize() + ":", resources[resource], "dollars")

def check_resources(drink,resource_list):
        """
        Check the available ingredients against whats needed for a drink
        Arguments: 'drink' selected, and 'resources' list 
        """
        for ingredient in drink["ingredients"]:
            if resource_list[ingredient] < drink["ingredients"][ingredient]:
                print(f"Not enough {ingredient} to make a your drink , please select something else")
                return False
        return True 

def process_coins(drink):
    """
    This coffee machine is strictly coin operated.
    In Canada, there are two additional coins - a Loonie($1) and Toonie($2) beyond that of the 
    quarter, dime, nickel and penny (which we have abolished) 

    Parameters: 'drink' - the users drink 

    """
    cost = drink["cost"] 
    coins = {"Nickels": 0, "Dimes": 0, "Quarters": 0, "Loonie": 0, "Toonie": 0}
    coin_total = 0
    for coin in coins:
        #get a coin name, ask how many of it youd like to put into the machine 
        current_coin = coins[coin]
        current_coin = int(input(f"how many {coin} would you like to put in?"))
        # Maths for coins 
        if coin == "Nickels":
            current_coin = current_coin * 0.05
        elif coin =="Dimes":
            current_coin = current_coin * 0.1
        elif coin == "Quarters":
            current_coin = current_coin * 0.25
        elif coin == "Toonie":
            current_coin = current_coin * 2.00

        coin_total += current_coin

    #Based off coins given, return change , thank user, or ask for a different choice     
    if coin_total < cost:
        print("Sorry not enough money for this drink :(")
        return 0 
    elif coin_total > cost:
        print("Thank you for your purchase!")
        change = round(coin_total - cost, 2)
        print(f"Your change is {change}")
        return cost 
    else:
        print("Thank you for your purchase!")
        return cost

def main_menu():
    """
    The Main Menu of the coffee machine program. 
    Parameters: None 
    Return: Bulk of the program, main menu and calls to the rest of the functions to make the coffee machine operate
    """
    finished = False

    while not finished:

        #Print Logo & Welcome Menu 
        print(logo)
        print("""
        Welcome! What kind of drink would you like?
        - Espresso
        - Latte
        - Cappuccino 
        """)

        #Enter and record menu choice
        menu_choice = input("> ").lower() 

        # Turn the Machine off
        if menu_choice == 'off':
            finished = True
        
        # Report Menu Choice 
        if menu_choice == "report":
            report()
            input("Enter to continue...")

        # Handle the drinks
        else:
            # Change shorthand answers
            if menu_choice.startswith("esp"):
                menu_choice = "espresso"
            elif menu_choice.startswith("lat"):
                menu_choice = "latte"
            elif menu_choice.startswith("cap"):
                menu_choice ="cappuccino"
                
            user_drink = MENU[menu_choice]
    
            # Added drink cost, for the sake of the user 
            print(f"Your {menu_choice.capitalize()} will cost {user_drink['cost']}")

            # Check resources, if available take coins 
            if check_resources(user_drink,resources):
                resources["cash"] += process_coins(user_drink)
            
                for ingredient in resources:
                    if ingredient in user_drink["ingredients"]:
                        resources[ingredient] -= user_drink["ingredients"][ingredient]
                        
                print(f"Enjoy your {menu_choice}☕~")
        
            # Ask for valid input
            else:
                print("Enter a valid choice")
                print(menu_choice)
        
main_menu()