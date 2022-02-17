###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import math as m
import turtle as t
import random as r

rgb_colors = []
colors = colorgram.extract('Daily Projects\Day 18 - Hirst Painting\\aqua_fanart.png', 200)
for color in colors:
    rgb_colors.append(color.rgb)

def get_color():
    """Get a color from the list of colors generated by the colorgram.py earlier

    Returns:
        tuple: red green and blue values to be used by the Turtle
    """
    choice = r.choice(rgb_colors)
    red = choice[0]
    green = choice[1]
    blue = choice[2]
    color_code = (red,green,blue)

    return color_code

def horiz_dots(num_columns):
    """Draw dots horizontally across the screen
    """
    for i in range(0,int(num_columns)):
        timmy.pendown()
        timmy.dot(50,get_color())
        timmy.penup()
        timmy.forward(100)

def go_down():
    """Go down while offscreen
    """
    if timmy.xcor() > 0:
        timmy.rt(90)
        timmy.forward(100)
        timmy.rt(90)
        timmy.forward(100)
    if timmy.xcor() < 0: 
        timmy.lt(90)
        timmy.forward(100)
        timmy.lt(90)
        timmy.forward(100)

def set_screen():
    """Set the initial screen size and color

    Returns:
        Screen: the Screen for the Turtle to darw on
    """
    screen = t.Screen()
    t.screensize(640,640,"grey10")
    return screen

def set_turtle():
    """ Instantiates the Turtle, sets the Turtles color, and positions it to start drawing from the top left

    Returns:
        Turtle: The Turtle we are going to be using to draw
    """
    t.colormode(255)
    timmy = t.Turtle()
    timmy.shape('triangle')
    timmy.color((0,255,255))
    timmy.penup()
    timmy.speed('fastest')
    timmy.setx(-600)
    timmy.sety(500)
    return timmy

# Setup screen and timmy
screen = set_screen()
timmy = set_turtle()

# Ask user for number of rows they'd like to have 
num_rows = int(m.floor(float(input("How many rows of dots would you like there to be?"))))
num_columns = int(m.floor(float(input("How many columns of dots would you like there to be? "))))

for i in range(0,int(num_rows/2)):
    horiz_dots(num_columns)
    go_down()
    horiz_dots(num_columns)
    go_down()

screen.exitonclick()