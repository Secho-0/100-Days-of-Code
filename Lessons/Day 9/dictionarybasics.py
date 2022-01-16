##Python Dictionaries

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
}

#Retrieving items from dictionary.
# print(programming_dictionary["Function"])

#Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."

#Create an empty dictionary.
empty_dictionary = {}

#Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

#Loop through a dictionary
# for key in programming_dictionary:
#   print(key)
#   print(programming_dictionary[key])


nesttest = {"France": "Paris", 
            "Germany": "Berlin",
}

# Nesting list in a dictionary
travel_log = {
    "France": ["Paris","Lille","Dijon"],
    "Germany": ["Berlin","Stuttgart","Hamburg"]
    }


# List in a dict in a dict
travel_log = {
    "France": {"cities_visited": ["Paris","Lille","Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin","Stuttgart","Hamburg"], "total_visits": 9}
    }


# Dict in a list 

travel_log = [
    {"Country":"France",
    "cities_visited": ["Paris","Lille","Dijon"], 
    "total_visits": 12},

    {"Country":"Germany", 
    "cities_visited": ["Berlin","Stuttgart","Hamburg"], 
    "total_visits": 9}
]

print(travel_log)
