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
from os import system

# Potential alternatives for animals 
animal_alternatives = {
    "dog":["puppy","dawg","dog","hound",
         "pooch","canine","fur baby","mutt"],
    "cat":["kitty","kitten","cat",
        "feline","fur baby","tabby"],
    "bird":["songbird","warbler","raptor",
        "feathered friend","birdie","fowl"]
    }


def get_info():
    """Get the Users Information, to work with potential band names
     as well as the number of band names wanted 

    Returns:
        list: user_info -> all the information provided except for the number of names wanted
        int: names_wanted -> the number of names the user wants to generate
    """
    user_city = input("Where did you grow up?\n")
    user_pet = input("What is your pets name?\n")
    user_animal = input(f"what kind of animal is {user_pet}?\n")
    user_color = input("What is your favourite color?\n")
    names_wanted = int(input("How many names do you want to generate?\n"))
   
    user_info = [user_city,user_pet,user_color,user_animal]

    return user_info, names_wanted

def get_word(user_info):
    """Get a word from the users info

    Args:
        user_info (list): the users information provided earlier

    Returns:
        str: word -> a random string from within the user_info list
    """
    word = r.choice (user_info)
    return word 
    
def generate_name(user_info: list,names_wanted: int):
    """Generate a band name based off the information provided by the user

    Args:
        user_info (list): informatione gathered earlier on, hometown, pet info, and favourite color
        names_wanted (int): how many names the user wishes to generate

    Returns:
        list: band_names -> the list of band names generated
    """
    band_names= []
    band_name = ""
    #get the length of userinfo provided
    listlen = len(user_info)
    #start working on as many bandnames as possible max -> names_wanted
    for i in range(names_wanted):
        #try a word for every item in the list
        for j in range(listlen):
            #Choose a word from the users info
            word = r.choice(user_info).lower()
            #Choose an alternate word for their animal for variety
            if word in animal_alternatives:
                word = r.choice(animal_alternatives[word])
            #while the word is not in the new band name, add it (and title case)
            while word.title() not in band_name:
                band_name += (word.title() + " ")
        #Add a band_name to the list of potential suggestions 
        if band_name not in band_names:
            band_names.append(band_name)
        #reset bfor next name 
        band_name = ""
    return band_names


running = True
while running:
    # Print Greeting
    print("Welcome to the Band Name Generator ")
    print("Lets go ahead and get your info!")

    # Gather User Info & Names wanted 
    all_info = get_info()

    # Set user info and names wanted 
    user_info = all_info[0]
    names_wanted = all_info[1]

    # Generate names and print results in a list 
    names = generate_name(user_info,names_wanted)
    print("Alright... hear us out why dont you try:")
    for i,name in enumerate(names):
        # end line on 5th name
        if i % 5 == 0:
            print(f"{name}?\n")
        # make sure a ? appears at the end of the list regardless of length 
        elif i == max(range(len(names))):
            print(f"{name}?")
            input("> Enter to CLEAR SCREEN...")
            system("cls")
        # main list items , seperated by pipes '|'
        else:
            print(f"{name}",end= " | ")
