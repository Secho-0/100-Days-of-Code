# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combonames = name1.lower() + name2.lower()

t = combonames.count("t")
r = combonames.count("r")
u = combonames.count("u")
e = combonames.count("e")
first_digit = t + r + u + e

l = combonames.count("l")
o = combonames.count("o")
v = combonames.count("v")
e = combonames.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if 90 < score > 10:
    print(f"Your score is {score}, you go together like coke and mentos.")

elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")

else:
    print(f"Your score is {score}.")