'''
Day 3 - Control Flow
- if/else statements
- Logic operators
- Modulo symbol
'''


print("Welcome to the Rollercoaster~")

height = int(input("What is your height in centimeters?\n> "))

if height > 120:
    print("Welcome aboard!")

else:
    print("I'm sorry commander, the risk is too great for you to board")


# List of comparison operators
# == - exactly equal to
# != - not equal to
# < or > - less than and greater than
# <= or >= - less than or equal to and equal to and less than


# basic rundown of how modulo works
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print('This is an even number.')
else:
    print('This is an odd number.')

if number % 3 == 0:
    print('This is divisible by 3')
else:
    print('This is not divisible by 3')


# nested if statements

print("Welcome to the Rollercoaster~")

height = int(input("What is your height in centimeters?\n> "))

if height > 120:
    print("Welcome aboard!")
    age = int(input("How old are you?"))
    if age >= 18:
        print("Your ticket costs $12")
    elif 12 <= age < 18:
        print("Your ticket costs $7")
    else:
        print("Your ticket costs $5")

else:
    print("I'm sorry commander, the risk is too great for you to board")

## Nested Ifs
height = int(input("What is your height in centimeters?\n> "))
if height > 120:
    print("Welcome aboard!")
    age = int(input("How old are you?"))
    bill = 0
    if 45 < age > 55:
        print("Your ticket is free!")
    elif age >= 18:
        print("Your ticket costs $12")
        bill += 12
    elif 12 <= age < 18:
        print("Your ticket costs $7")
        bill += 7
    else:
        print("Your ticket costs $5")
        bill += 5

    want_photo = input("Do you want a photo to commemorate the event? Y / N")
    if want_photo.lower().startswith('y'):
        bill += 3
    else:
        print("We hope you enjoyed the ride~!")
    print(f"Your bill total is {bill}")
else:
    print("I'm sorry commander, the risk is too great for you to board")

# Logical Operators

# and | or | not
# a and b needs both a and b set to true to be true
# a or b needs one of a or b set to true to be true
# a not b requires strictly a to be set to true, and not b, to be true