from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)

def goUp():
    newY = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), newY)

def goDown():
    newY = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), newY)

screen.listen()
screen.onkey(goUp, "w")
screen.onkey(goDown, "s")

gameIsOn = True
while gameIsOn:
    screen.update()

screen.exitonclick()