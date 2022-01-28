'''
#
# Day 1 - Final Project
# --- BAND NAME GENERATOR ---
# Goals:
# 1) Create a Greeting
# 2) Ask for the City the user grew up in
# 3) Ask for the name of their pet
# 4) Combine the City + Pet names to get a potential band name
# 5) Input Cursor should appear on a new line when user is prompted


print("Welcome! Let's help you get a potential band name!")

user_city = input("What city did you grow up in?\n")
user_pet = input("What is your pets name?\n")

band_name = (user_city + " " + user_pet)
print("You should call your band " + band_name + ".")
'''

import random as r


animal_alternatives = {
    "dog":["puppy","dawg","dog","hound","pooch","canine","fur baby","mutt"],
    "cat":["kitty","kitten","cat","feline","fur baby","tabby"],
    "bird":["songbird","warbler","raptor","feathered friend","birdie","fowl"]
    }


def get_info():
    user_city = input("Where did you grow up?\n")
    user_pet = input("What is your pets name?\n")
    user_animal = input(f"what kind of animal is {user_pet}?\n")
   
    names_wanted = int(input("How many names do you want to generate?\n"))
   
    user_info = [user_city,user_pet,user_animal]

    return user_info, names_wanted

def get_word(user_info):
    word = r.choice (user_info)
    return word 
    
def generate_name(user_info: list,names_wanted: int):
    band_names= []
    band_name = ""
    ct = 0

    while ct <= names_wanted:
        i = 0
        while i <= 3:
            word = r.choice(user_info)
            if word in animal_alternatives:
                word = r.choice(animal_alternatives[word])
                if word not in band_name:
                    band_name += (word + " ")
            i += 1
        if band_name not in band_names:
            band_names.append(band_name)
        band_name = ""
        ct += 1  
    return band_names


running = True
while running:
    print("Welcome to the Band Name Generator ")
    print("Lets go ahead and get your info!")

    all_info = get_info()
    user_info = all_info[0]
    names_wanted = all_info[1]
    names = generate_name(user_info,names_wanted)

    print("Alright... hear us out why dont you try:")
    for name in names:
        print(f"{name}?")
