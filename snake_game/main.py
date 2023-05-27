from turtle import Turtle, Screen
import time
screen = Screen()
# screen setup
screen.setup(width=600, height=600)
# screen background
screen.bgcolor("black")
# screen title
screen.title("Snake Game")
# turn off tracer
screen.tracer(0)
# 3 single snake position
positions = [(0, 0), (-20, 0), (-40, 0)]
snakes = []

for number in range(3):
    snake = Turtle(shape="square")
    snakes.append(snake)
    snake.color("white")
    snake.penup()
    snake.goto(positions[number])


game_on = True
while game_on:
    # update the whole snake
    screen.update()
    # delay
    time.sleep(0.1)
    for number in range(len(snakes) - 1, 0, -1):
        # the snake replaced by
        x = snakes[number - 1].xcor()
        y = snakes[number - 1].ycor()
        snakes[number].goto(x, y)
    snakes[0].forward(20)


















screen.exitonclick()