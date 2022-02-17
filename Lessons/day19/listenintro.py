import turtle as t

timmy = t.Turtle()
screen = t.Screen()

screen.listen()

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.back(10)

def turn_left():
    timmy.lt(10)
    
def turn_right():
    timmy.rt(10)

def clear_screen():
    timmy.speed("fastest")
    timmy.penup()
    timmy.clear()
    timmy.home()
    timmy.pendown()
    timmy.speed(6)

screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear_screen,"c")

screen.exitonclick()