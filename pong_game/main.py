from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
import random
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
# scoreboard right
scoreboard_right = ScoreBoard()
# scoreboard left
scoreboard_left = ScoreBoard()

# key control
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_on = True
while game_on:
    # update screen
    screen.update()
    # delay the ball
    time.sleep(ball.ball_speed)
    # ball move
    ball.move()
    # collision on top or bottom wall
    if (ball.ycor() > 280) or (ball.ycor() < -280):
        ball.bounce()
    # collision with paddle
    if (ball.xcor() >= 330 or ball.xcor() <= -330) and \
            (ball.distance(right_paddle) < 50 or ball.distance(left_paddle) < 50):
        ball.catch()
    # miss right paddle
    if ball.xcor() > 380:
        ball.reset()
        scoreboard_left.l_win()
    # miss left paddle
    if ball.xcor() < -380:
        ball.reset()
        scoreboard_right.r_win()






screen.exitonclick()