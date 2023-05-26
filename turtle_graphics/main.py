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
# for number in range(3, 11):
#     r = random.randint(0, 255)
#     b = random.randint(0, 255)
#     g = random.randint(0, 255)
#     timmy.pencolor(r, g, b)
#     for _ in range(number):
#         timmy.forward(100)
#         timmy.right(360/number)

# turtle random walk
# def random_walk():
#     r = random.randint(0, 255)
#     b = random.randint(0, 255)
#     g = random.randint(0, 255)
#     s = random.randint(0, 10)
#     timmy.pencolor(r, g, b)
#     timmy.pensize(width=10)
#     timmy.speed(s)
#     timmy.forward(30)
#     degree = random.choice([0, 90, 180, 270])
#     timmy.setheading(degree)
#
#
# for _ in range(1000):
#     random_walk()


# def random_color():
#     r = random.randint(0, 255)
#     b = random.randint(0, 255)
#     g = random.randint(0, 255)
#     color = (r, g, b)
#     return color


def draw_spirograph():
    timmy.speed(0)
    for angle in range(0, 361, 4):
        timmy.pencolor(random_color())
        timmy.setheading(angle)
        timmy.circle(50)


draw_spirograph()

my_screen.exitonclick()
# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
# print(table)
