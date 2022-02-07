from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        """uses Turtle __init__ , sets up ScoreBoard to be at the top center,
         with an initial score of 0
        """
        super().__init__()
        
        self.score = 0
        self.color("white")
        self.speed('fastest')
        self.penup()
        self.hideturtle()
        self.goto(0,480)
        self.write(f"Score: {self.score}",align = 'center',font = ['Arial',12,'normal'])

    def score_up(self):
        """Clear the previous score and write the new one 
        """
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}",align = 'center',font = ['Arial',12,'normal'])
    
    def game_over(self):
        """Print Game Over in the middle, dont erase score
        """
        self.goto(0,0)
        self.write("G A M E O V E R",align= "center", font=['Arial',24,'bold'])