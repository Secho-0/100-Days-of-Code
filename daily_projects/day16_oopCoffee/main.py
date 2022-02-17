from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import COFFEE as logo

menu = Menu()
register = MoneyMachine()
coffee_maker = CoffeeMaker()
on = True

while on:
    print(logo)
    user_choice = input(f"""What would you like to drink?
    {menu.get_items()}
    > """).lower()
    if user_choice == "off":
        print("Thank you for getting your coffee with us today! Buh-bye!")
        on = False
    elif user_choice == "report":
        coffee_maker.report()
        register.report()
    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink):
            if register.make_payment(drink.cost):        
                coffee_maker.make_coffee(drink)