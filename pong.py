from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import score
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.tracer(0)
r=Paddle((350, 0))
l=Paddle((-360, 0))
tim=Turtle()
b=Ball()
sc=score()
screen.listen()
screen.onkey(r.up, 'Up')
screen.onkey(r.down, 'Down')
screen.onkey(l.up, 'w')
screen.onkey(l.down, 's')
ison=True
while ison:
    time.sleep(b.move_speed)
    screen.update()
    b.move()
    # screen.write(f"Score : {left}", align="center", font=("Arial", 24, "normal"))
    if b.ycor() > 280 or b.ycor() < -280:
        b.hitwall()
    if b.distance(r) < 50 and b.xcor() > 320 or b.distance(l) < 50 and b.xcor() < -320:
        b.bouncex()
    if  b.xcor()>380:
        sc.lpoint()
        b.reseet()
    if b.xcor()<-380:
        sc.rpoint()
        b.reseet()

screen.exitonclick()