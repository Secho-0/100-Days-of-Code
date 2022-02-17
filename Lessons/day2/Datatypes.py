'''
Day 2 - Data Types
- Primitive Datatypes - int str bool
- Type Error, Type Checking, Type Conversion
- F Strings
'''

# integer
i = 123
# float
f = 1.23
# boolean
b = True
# string
s = "strings"


num_char = len(input("What is your name?"))

#  print("Your name has " + num_char + " characters.")
#  #this breaks because num_char is an integer not a string, and you cannot concatenate different data types

# use the 'type' function and print it on a variable to discover what its datatype is
print(type(num_char))

s_numchar = str(num_char)
print(s_numchar)

fl_numchar = float(num_char)

print("this is an integer: {} \nthis is a string: {}\nthis is a float: {}".format(num_char, s_numchar, fl_numchar))




