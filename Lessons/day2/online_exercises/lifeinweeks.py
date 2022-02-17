# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

time_remaining = 90 - int(age)

days_remain = time_remaining * 365
weeks_remain = time_remaining * 52
months_remain = time_remaining * 12

print("You have {} days, {} weeks, and {} months left.".format (days_remain, weeks_remain, months_remain))

