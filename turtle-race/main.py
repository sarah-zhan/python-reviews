from turtle import Turtle, Screen
import random
# turtle = Turtle(shape="turtle")
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="What is your bet?", prompt="Enter a color to bet which turtle to win the game, "
                                                         "red/yellow/green/blue/purple/orange? ")
game_on = False

colors = ["red", "yellow", "green", "blue", "purple", "orange"]
positions = [(-230, -150), (-230, -100), (-230, -50), (-230, 0), (-230, 50), (-230, 100)]
turtles = []
for number in range(6):
    turtles.append(Turtle(shape="turtle"))
    turtles[number].color(colors[number])
    turtles[number].penup()
    turtles[number].goto(positions[number])


if bet:
    game_on = True

while game_on:
    for turtle in turtles:
        if turtle.xcor() == 240:
            winner = turtle
            if bet.lower() == winner.pencolor():
                print("You win.")
                print(f"The winner is {winner.pencolor()}.")
                game_on = False
            else:
                print("You lose.")
                print(f"The winner is {winner.pencolor()}.")
                game_on = False
        turtle.forward(random.randint(0, 10))
        turtle.speed(random.randint(0, 10))


screen.exitonclick()
