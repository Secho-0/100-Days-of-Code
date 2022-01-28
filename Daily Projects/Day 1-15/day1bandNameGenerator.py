'''
Day 1 - Final Project
--- BAND NAME GENERATOR ---
Goals:
1) Create a Greeting
2) Ask for the City the user grew up in
3) Ask for the name of their pet
4) Combine the City + Pet names to get a potential band name
5) Input Cursor should appear on a new line when user is prompted
'''


print("Welcome! Let's help you get a potential band name!")

user_city = input("What city did you grow up in?\n")
user_pet = input("What is your pets name?\n")

band_name = (user_city + " " + user_pet)
print("You should call your band " + band_name + ".")
