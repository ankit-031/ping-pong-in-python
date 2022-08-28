from turtle import  Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove=10
        self.ymove=10
        self.move_speed = 0.1
    def move(self):
        x=self.xcor()+self.xmove
        y=self.ycor()+self.ymove
        self.goto(x,y)


    def hitwall(self):
            self.ymove *= -1

    def bouncex(self):
        self.xmove *= -1
        self.move_speed *= 0.8
    def reseet(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bouncex()

