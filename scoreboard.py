from turtle import Turtle,Screen



class score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore=0
        self.rscore=0
        self.updatel()
    def updatel(self):
        self.clear()
        self.goto(-175, 200)
        self.write(f"Score : {self.lscore}", align="center", font=("Arial", 40, "normal"))
        self.goto(175, 200)
        self.write(f"Score : {self.rscore}", align="center", font=("Arial", 40, "normal"))

    def lpoint(self):
        self.lscore +=1
        self.updatel()
    def rpoint(self):
        self.rscore +=1
        self.updatel()
