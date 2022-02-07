from turtle import Turtle

# Setup constants for the snake
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):
    """Snake for the snake game

    Args:
        Turtle (Turtle): Turtle Class from the turtle apckage
    """
    def __init__(self):
        """ Create a snake, and set the head of it to the first turtle 
        """
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape('triangle')

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("cyan2")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def create_segment(self):
        new_segment = Turtle("square")
        new_segment.color("cyan2")
        new_segment.penup()
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)
        if (len(self.segments)-1) % 5 == 0:
            self.segments[-1].shape('turtle')

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
