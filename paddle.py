from turtle import Turtle,Screen

class Paddle(Turtle):
    def __init__(self,positon):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(positon)

    def up(self):
        angle = self.ycor()
        angle += 30
        self.goto(self.xcor(), angle)

    def down(self):
        angle = self.ycor()
        angle -= 30
        self.goto(self.xcor(), angle)

