'''
Day 2 - Mathematical operations

Example of order of operations in python
P E M D A S
Parenthesis -  ()
  Exponents -  **
  Mult| Div - * | /
  Add | Sub - + | -
'''
pemdas = 5 + 3 * (52 - 16 / 4 - 5 ** 1 * 2)
print(pemdas)

# you can round both variables and operations
print(round(pemdas))

# you can also use type function
print(type(pemdas))

# variables always carry the result of a sum
pemdas += 3
print(pemdas)
pemdas /= 4
print(pemdas)
