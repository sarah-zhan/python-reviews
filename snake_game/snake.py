from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_snake(position)

    def add_snake(self, position):
        snake = Turtle(shape="square")
        self.snakes.append(snake)
        snake.color("white")
        snake.penup()
        snake.goto(position)

    def extend(self):
        self.add_snake(self.snakes[-1].position())

    def move(self):
        for number in range(len(self.snakes) - 1, 0, -1):
            # the snake replaced by the next snake, the last one to guide
            x = self.snakes[number - 1].xcor()
            y = self.snakes[number - 1].ycor()
            self.snakes[number].goto(x, y)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
