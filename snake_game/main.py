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



game_on = True
while game_on:
    # update the whole snake
    screen.update()
    # delay
    time.sleep(0.1)



















screen.exitonclick()