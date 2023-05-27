from turtle import Turtle, Screen
import time
from snake import Snake
screen = Screen()
# screen setup
screen.setup(width=600, height=600)
# screen background
screen.bgcolor("black")
# screen title
screen.title("Snake Game")
# turn off tracer
screen.tracer(0)

snake = Snake()

# use keyboard to change the direction
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    # update the whole snake
    screen.update()
    # delay
    time.sleep(0.1)
    snake.move()


















screen.exitonclick()