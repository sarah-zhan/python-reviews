from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
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
food = Food()
scoreboard = ScoreBoard()
# initial scoreboard
scoreboard.write(f"Score: {scoreboard.score}", move=False, align="center", font=("Arial", 11, "normal"))
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

    # detect collision
    if snake.head.distance(food) < 15:
        food.move()
        # clear the record
        scoreboard.clear()
        # update the score
        scoreboard.score += 1
        # show the scoreboard again
        scoreboard.write(f"Score: {scoreboard.score}", move=False, align="center", font=("Arial", 11, "normal"))

















screen.exitonclick()