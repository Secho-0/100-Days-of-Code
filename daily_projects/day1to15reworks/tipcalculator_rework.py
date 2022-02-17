'''

Day 2 - Final Project
--- TIP CALCULATOR  ---
Goals:
1) Create a Greeting
2) Ask for the bill total
3) Ask for the tip percentage
4) Ask how many people will split the bill
5) Give total, with cents


welcome = 'Welcome~ \n This is a tool to help you calculate basic tip,and bill split amongst a group'

print(welcome)

bill_total = float(input("What was your bill total? "))
tip_percent = float(input("What percentage would you like to tip? "))/100
diners = int(input("How many people are splitting the bill? "))

bill_split = round(bill_total / diners,2)
tip_amount = round(bill_total * tip_percent,2)

tip_split = round(tip_amount / diners,2)

bill_tip_split = round(bill_total * (1+tip_percent)/ diners, 2)

print(f"For a bill of {bill_total} , each of the {diners} diners will pay ${bill_tip_split}.")
print(f"This ends up being:\n ${bill_split} for food, and ${tip_split} for tip.")
'''
def calc_tip( diners: int, bill_before: float, tip_percent: float):
    """Calculate tip per person

    Args:
        diners (int): Number of people in attendance to the meal
        bill_before (float): What was the bill total before tip?
        tip_percent (float): What percentage would you like to tip - whole number

    Returns:
        float: tip -> the tip amount on its own
               tip_per_person -> the amount each person needs to tip independently 
    """
    tip = round(bill_before * tip_percent, 2)
    tip_per_person = round(tip/diners, 2)
    return tip, tip_per_person

def calc_bill(diners: int, bill_before: float,  tip:float):
    """Calculate the total bill with tip

    Args:
        diners (int): Number of people in attendace to the meal
        bill_before (float): What was the bill before tip?
        tip (float): What is the tip amount?

    Returns:
        float: bill -> the total bill after tip has been added
               bill_per_person -> the total amount each person should pay 
    """
    bill = round(bill_before + tip, 2)
    bill_per_person = round(bill / diners, 2)
    return bill, bill_per_person

def get_info():
    """Get the information from the usr

    Returns:
        list: List of Diners, Bill before tip, and tip percentage
    """
    diners = int(input("How many people are dining?"))
    bill = float(input("What is your bill?"))
    tip_percentage = float(input("What Percentage(%) would you like to tip?"))/100
    user_info = [diners,bill,tip_percentage]

    return user_info


running = True
while running:
    # Welcome user
    print("It seems you may need some help with the bill , lets see what we can do ^^")

    # Get user info
    dinner_info = get_info()
    #Calculate tip and bills 
    tips = calc_tip(dinner_info[0],dinner_info[1],dinner_info[2])
    bills = calc_bill(dinner_info[0],dinner_info[1], tips[0])

    # Print results for users
    print(f"""
    For a bill of ${dinner_info[1]}:
        Each person should pay ${bills[1]} with tip included.
        The total tip will be ${tips[0]}
        The original bill was ${dinner_info[1]}
        The total with tip is ${bills[0]}
    """)
    
    # Ask to run again 
    runagain = input("Would you like to run again? (Y)es or (N)o\n>>> ").lower()

    if runagain.startswith('y'):
        continue
    else:
        running = False
        break

