import time, snake
from turtle import Screen


# Setup the screen for people to play
screen = Screen()
screen.tracer(0)
screen.setup(1000,1000)
screen.bgcolor("grey10")
screen.title("I Guess We're Making Snake")

# Setup player
player = snake.Snake()

# Setup Keystrokes 
screen.listen()
screen.onkey(player.up,"Up")
screen.onkey(player.left,"Left")
screen.onkey(player.down,"Down")
screen.onkey(player.right,"Right")



snake = True
while snake:
    screen.update()
    time.sleep(0.3)



    player.move()
    

screen.exitonclick()