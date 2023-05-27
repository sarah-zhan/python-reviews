from turtle import Turtle, Screen

# turtle = Turtle(shape="turtle")
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="What is your bet?", prompt="Enter a color to bet which turtle to win the game, "
                                                         "red/yellow/green/blue/purple/orange? ")


def make_turtle():
    colors = ["red", "yellow", "green", "blue", "purple", "orange"]
    positions = [(-230, -150), (-230, -100), (-230, -50), (-230, 0), (-230, 50), (-230, 100)]
    turtles = []
    for number in range(6):
        turtles.append(Turtle(shape="turtle"))
        turtles[number].color(colors[number])
        turtles[number].penup()
        turtles[number].goto(positions[number])


make_turtle()
screen.exitonclick()
