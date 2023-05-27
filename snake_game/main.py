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
turtles = []

for number in range(3):
    turtle = Turtle(shape="square")
    turtles.append(turtle)
    turtle.color("white")
    turtle.penup()
    turtle.goto(positions[number])


game_on = True
while game_on:
    # update the whole snake
    screen.update()
    # delay
    time.sleep(0.1)
    for turtle in turtles:
        turtle.forward(20)

















screen.exitonclick()