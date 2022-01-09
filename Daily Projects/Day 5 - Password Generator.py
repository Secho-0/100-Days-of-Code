'''
Day 5 - Password Generator
- How many letters in your password
- How many symbols
- How many letters
'''

#  Generator Project
import random as r
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ''
for i in range(0,nr_letters):
    password += r.choice(letters)

for i in range(0, nr_symbols):
    password += r.choice(symbols)

for i in range(0, nr_numbers):
    password += r.choice(numbers)
print(password)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

pw_list = []
pw = ''
for i in range(0,nr_letters):
    pw_list.append(r.choice(letters))

for i in range(0, nr_symbols):
    pw_list.append(r.choice(symbols))

for i in range(0, nr_numbers):
    pw_list.append(r.choice(numbers))

for i in range(0, len(pw_list)):
    digit = pw_list.pop(r.randint(0,len(pw_list)-1))
    pw += digit
print(pw)
