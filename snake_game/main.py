from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

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
    for turtle in turtles:
        turtle.forward(100)
















screen.exitonclick()