"""Intro to importing modules, utilizes the 'turtle' module to teach basic OOP concepts, and how to use modules"""
import turtle

george = turtle.Turtle()
#george = Turtle() # This is how to use the turtle class if "from turtle import Turtle" is used above

george.shape('turtle')
george.color('RoyalBlue2')

## Attribute calling, and method calling
my_screen = turtle.Screen()
print(my_screen.canvheight)
george.forward(100)

my_screen.exitonclick()