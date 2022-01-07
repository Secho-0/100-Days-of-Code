'''
Day 4 - Lists
- useful for storing sets of similar data
- can use a specific order of things FIFO for example
- uses [] brackets with items seperated by ,
'''

fruits = ['apple' ,'banana', 'cherry']

westernstates = [ 'Washington', 'Oregon', 'California','Nevada']
# order of list items matters and is perpetual and order will be stored


'''
items in lists start with 0 instead of 1 for the first item
the index number can be best looked at as steps shifted to get to the item
however , negative indexes also work because of this principle
i.e. 
- 0 is the start of the list 
- 1 is one step away from the first item 
- 2 is twop steps away from the start
 
- -1 is the very end of the list in our 


'''

# Will print out Washington
print(westernstates[0])

# Append will add to the end of a list
westernstates.append("Arizona")

print(westernstates)

# Extend will add a list to the end of the targeted list
westernstates.extend(["New Mexico", "Utah"])
print(westernstates)

dirty_dozen = ["Strawberries","Spinach", "Kale", "Nectarines", "Apples", "Grapes",
               "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes"]

