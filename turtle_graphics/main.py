from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
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
for _ in range(10):
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)






my_screen = Screen()
my_screen.exitonclick()


# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
# print(table)
