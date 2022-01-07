'''
Day 4 - Random Module
- Pythons Random Module uses Mersenne Twister
- 'import' is used to import various modules
'''

import random as r

rand_int = r.randint(1, 10)
print(rand_int)

# 0.0000000000 - 0.999999999
rand_float = r.random()
print(rand_float)

# 0.000000 - 4.9999999
rand_float = r.random() * 5
print(rand_float)

#using for love score
lovescore = r.randint(1,100)
print(f"Your lovescore is {lovescore}")
