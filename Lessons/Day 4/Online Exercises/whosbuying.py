import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

choice = random.randint(0,(len(names) -1))
buyer = names[choice]

print(f"{buyer} is going to buy the meal today!")

# this can be simplified to
# the reason we use the above is to teach indexes

buyer = random.choice(names)
print(f"{buyer} is going to buy the meal today!")
