from turtle import Turtle, Screen
from paddle import RightPaddle
# set up the screen
screen = Screen()
screen.tracer(30)
screen.listen()
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

game_on = True
while game_on:
    # key control
    screen.onkey(right_paddle.up, "Up")
    screen.onkey(right_paddle.down, "Down")
    # update screen
    screen.update()






screen.exitonclick()