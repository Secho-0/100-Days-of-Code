'''
Day 1 - Input Function & Variables
- Input can be executed within a print function
- Variables can store information both declared and user entered
'''

print("Hello, " + input("What is your name?") + "!\n\n")

# Declaring a variable by input
my_name = input("What is your name?")
# Declaring a variable
my_lastname = 'B'

# Using variables
print("Hello~, Nice to meet you " + my_name)
# Input that is not stored, as well as how to concatenate Int + Str variables
input("Did you know that your name is " + str(len(my_name)) + " letters long?")
# Using both declared Variables
print(my_name + " " + my_lastname + ". Is your full name according to your records.")