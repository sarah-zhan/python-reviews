from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
# set up the screen
screen = Screen()
screen.tracer(0)
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
right_paddle = Paddle((350, 0))
# left paddle
left_paddle = Paddle((-350, 0))
# ball
ball = Ball()
# key control
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_on = True
while game_on:
    # delay the ball
    time.sleep(0.1)
    # ball move
    ball.move()
    # update screen
    screen.update()
    # collision on top or bottom wall
    if (ball.ycor() > 290) or (ball.ycor() < -290):
        ball.bounce()








screen.exitonclick()