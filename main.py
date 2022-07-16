from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

lPaddle = Paddle((-350, 0))
rPaddle = Paddle((350, 0))

screen.listen()
screen.onkey(lPaddle.goUp, "w")
screen.onkey(lPaddle.goDown, "s")
screen.onkey(rPaddle.goUp, "Up")
screen.onkey(rPaddle.goDown, "Down")

gameIsOn = True
while gameIsOn:
    screen.update()

screen.exitonclick()