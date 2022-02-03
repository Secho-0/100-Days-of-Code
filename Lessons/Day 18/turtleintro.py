#####Turtle Intro######

import turtle as t
import random as r

timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("cyan2")
timmy.pensize(30)
timmy.speed(0)
t.colormode(255)




# timmy_the_turtle.forward(100)
# timmy_the_turtle.backward(200)
# timmy_the_turtle.right(90)
# timmy_the_turtle.left(180)
# timmy_the_turtle.setheading(0)

######## Challenge 1 - Draw a Square ############

# for i in range(4):
#     timmy.forward(100)
#     timmy.left(90)


########### Challenge 2 - Draw a Dashed Line ########

# for i in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

########### Challenge 3 - Drawing Different Shapes ########

# numsides = 3
# while numsides <= 10:
#     angle = 360/numsides
#     timmy.pencolor(colors.pop(colors.index(r.choice(colors))))
#     for sides in range(numsides):
        
#         timmy.forward(100)
#         timmy.right(angle)
#     numsides += 1    

########### Challenge 4 - Drawing Different Colors ########
def get_color():
    red = r.choice(range(0,256))
    green = r.choice(range(0,256))
    blue = r.choice(range(0,256))
    color_code = (red,green,blue)
    return color_code
    
# for i in range(1001):
#     timmy.color(get_color())
#     timmy.forward(50)
#     timmy.setheading(r.choice(movement))


########### Challenge 5 - Drawing Different Colored Circles ########

def draw_spiro(size_of_gap):
    for i in range(int(360/size_of_gap)):
        timmy.color(get_color())
        timmy.circle(100)
        current_heading = timmy.heading()
        timmy.setheading(current_heading + size_of_gap)

draw_spiro(5)

myScreen = t.Screen()
myScreen.exitonclick()
