from turtle import Turtle, Screen
import random
timmy = Turtle()
timmy.shape("turtle")
timmy.color("black")

# draw a square
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)

# draw a dash line
# for _ in range(10):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)

my_screen = Screen()

# Setting the screen color-mode
my_screen.colormode(255)
# draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon (3-10 sides)
for number in range(3, 11):
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    timmy.pencolor(r, g, b)
    for _ in range(number):
        timmy.forward(100)
        timmy.right(360/number)


my_screen.exitonclick()

my_screen = Screen()
my_screen.exitonclick()


# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
# print(table)
