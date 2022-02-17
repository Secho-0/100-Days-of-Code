from turtle import Turtle
import random as r
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color("aqua")
        self.penup()
        self.shapesize(0.5,0.5)
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        r_int = r.randint(-460,460)
        self.goto(r_int,r_int)