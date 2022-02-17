############DEBUGGING#####################

# # Describe Problem
# ANSWER: need to increase range(1,20) to range(1,21) as range is exclusive for the end number
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# ANSWER: Describe Problem
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# ANSWER: randint is inclusive, which is great but index start at 0, meaning that the dice_imgs[] has 0-5 not 1-6
# ANSWER: this can be fixed by changing the rang of randint to randint(0,5)
# ANSWER: OR subtracting one in the printto make the statement 'print(dice_imgs[dice_num-1])'
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# ANSWER: Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year =< 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# ANSWER: Play Computer 
# year = int(input("What yerar were you born?"))
# if 1980 < year <= 1994:
#     print("you are a millenial")
# elif year > 1994:
#     print("you are gen Z.")


# # Fix the Errors
# ANSWER: the print isnt indented nor is there a 'f' to represent a formatted string in the printstatement
# ANSWER: the age isnt an integer its a string int(input()) would fix this 
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# #ANSWER: Fix the Errors
# age = input("How old are you?")
# if age > 18:
#     print(f"You can drive at age {age}.")

# #Print is Your Friend
# ANSWER: word_per_page is set to 'equals' not 'equal to' - true maths, not declaration 
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# # ANSWER: Print is your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)


# #Use a Debugger
# ANSWER: This actually made me feel silly, the append is outside the for loop,
# ANSWER: which is why its only concerned about the last digit in the list
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])