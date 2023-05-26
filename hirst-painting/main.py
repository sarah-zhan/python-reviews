import colorgram

# rgb_colors = []
# colors = colorgram.extract('hirst.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)
# print(rgb_colors)
color_list = [(207, 159, 80), (55, 87, 130), (146, 91, 40), (140, 26, 50), (222, 207, 105), (132, 177, 202),
              (157, 46, 84), (46, 55, 103), (170, 160, 39), (130, 189, 144), (84, 20, 43), (37, 43, 68),
              (185, 95, 107), (186, 140, 169), (85, 119, 179), (195, 80, 71), (89, 157, 94), (60, 39, 33),
              (80, 152, 165), (52, 128, 125), (79, 75, 44), (162, 202, 218), (47, 73, 76), (220, 183, 167),
              (48, 74, 73), (219, 175, 187)]

# draw 10 x 10, different color dots
# dot is 20d, distance 50
from turtle import Turtle, Screen
import random
timmy = Turtle()
screen = Screen()
screen.colormode(255)


def draw_dot(distance, size):
    timmy.hideturtle()
    timmy.penup()
    timmy.goto(-200, -200)
    for i in range(size):
        for j in range(size):
            color = random.choice(color_list)
            timmy.dot(20, color)
            timmy.forward(distance)

        timmy.backward(distance * size)
        timmy.left(90)
        timmy.forward(distance)
        timmy.right(90)


draw_dot(50, 10)

screen.exitonclick()
