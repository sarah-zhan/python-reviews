from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

positions = [(0, 0), (-20, 0), (-40, 0)]
turtles = []
for number in range(3):
    turtles.append(Turtle(shape="square"))
    turtles[number].color("white")
    turtles[number].goto(positions[number])



















screen.exitonclick()