import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 270
SPEEDS = [1, 3, 6, 10, 0]
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# turtle
turtle = Player()
# listen to event
screen.listen()
screen.onkey(turtle.move, "Up")

# car
car = CarManager()

# scoreboard
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:

    time.sleep(0.2)
    screen.update()

    # cross the road
    if turtle.ycor() > FINISH_LINE_Y:
        turtle.back()
        car.speed_up()

    car.generate_car()
    car.move()

    # detect the distance (collision)
    for each in car.cars:
        if each.distance(turtle) < 20:
            print("Game Over")
            game_is_on = False







screen.exitonclick()