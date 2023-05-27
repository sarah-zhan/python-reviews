from turtle import Turtle, Screen
from paddle import RightPaddle
# set up the screen
screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)

turtle = Turtle()
turtle.hideturtle()
turtle.color("white")
turtle.penup()
turtle.goto(0, 300)
turtle.setheading(270)
for _ in range(30):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

# right paddle
right_paddle = RightPaddle()










screen.exitonclick()