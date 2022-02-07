import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from turtle import Screen


# Setup the screen for people to play
screen = Screen()
screen.tracer(0)
screen.setup(1000,1000)
screen.bgcolor("grey10")
screen.title("I Guess We're Making Snake")

# Setup player, food, and  Scoreboard
nomnoms = Food()
player = Snake()
score = ScoreBoard()
player_speed = 0.2

# Setup Keystrokes 
screen.listen()
screen.onkey(player.up,"Up")
screen.onkey(player.left,"Left")
screen.onkey(player.down,"Down")
screen.onkey(player.right,"Right")



snek = True
while snek:
    screen.update()
    time.sleep(player_speed)
    player.move()

    # What happens when you eat some food???
    if player.head.distance(nomnoms) < 15:
        nomnoms.refresh()
        score.score_up()
        player.create_segment()  
        player_speed -= 0.005

    # Check if in bounds
    if (player.head.xcor() > 480 or  player.head.xcor() < -480 
        or 
        player.head.ycor() > 480 or  player.head.ycor() < -480):
        snek= False
        score.game_over()

    # Check for tail collision
    for segment in player.segments[1:]:
        if player.head.distance(segment) < 10:
            snek = False
            score.game_over()

screen.exitonclick()