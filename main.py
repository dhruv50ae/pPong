from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

lPaddle = Paddle((-350, 0))
rPaddle = Paddle((350, 0))
ball = Ball()


screen.listen()
screen.onkey(lPaddle.goUp, "w")
screen.onkey(lPaddle.goDown, "s")
screen.onkey(rPaddle.goUp, "Up")
screen.onkey(rPaddle.goDown, "Down")

gameIsOn = True
while gameIsOn:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()

    if ball.distance(rPaddle) < 50 and ball.xcor() > 320 or ball.distance(lPaddle) < 50 and ball.xcor() < -320:
        ball.bounceX()

screen.exitonclick()