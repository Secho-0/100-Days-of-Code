'''
Day 4 - for loops
- How to iterate through loops
- we can execute full codeblocks within a for loop
'''

fruits = ["Apple", "Banana", "Cherry"]


for fruit in fruits:
    print(fruit)
    print(fruit + " pie~")


for i in range(1,11,3):
    print(i)



total = 0
for j in range(1, 101):

    total += j
print(total)
