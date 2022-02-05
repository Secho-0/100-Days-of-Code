from turtle import Turtle, Screen
import random as r

#Set starting positions and colors 
starting_ypos = [-75,-45,-15, 15, 45, 75]
colors = ['red','orange','yellow','green','blue','purple']

def create_turtles():
    turtles = []
    for turtle_index in  range(0,6):
        turtle = Turtle('turtle')
        turtle.penup()
        turtle.color(colors[turtle_index])
        turtle.goto(-230,starting_ypos[turtle_index])
        turtles.append(turtle)
    return  turtles     

screen = Screen()
screen.setup(width= 500, height= 250)
turtles = create_turtles()

user_bet = screen.textinput("Place A Bet","Which turtle do you think will win?\n>> ")
if user_bet:
    racing = True

while racing:
    for turtle in turtles:
        rand_distance = r.randint(0,10)
        turtle.forward(rand_distance)
        
        if turtle.xcor() >= 250:
            if turtle.pencolor() == user_bet.lower():
                print("You Win! Congrats")
                racing = False
            else:
                print(f"You lost :( {turtle.pencolor()} ended up winning")
                racing = False

screen.exitonclick()