'''
Day 6 - Function basics and While Loops
- Going over Python's built in functions and how to make our own
- while loops and theri basis

'''


#  exmaples of built in python functions
print("Hello")

num_char = len("hello")
print(num_char)

# defining a custom function
def myFunction():
    print("Hello")
    print("Bye")

# calling our custom function
myFunction()

numRuns = 5
while numRuns > 5:
    myFunction()
    numRuns -= 1
