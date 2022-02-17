'''

Day 2 - Final Project
--- TIP CALCULATOR  ---
Goals:
1) Create a Greeting
2) Ask for the bill total
3) Ask for the tip percentage
4) Ask how many people will split the bill
5) Give total, with cents
'''

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
