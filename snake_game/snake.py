from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]
        self.up()
        self.down()
        self.left()
        self.right()

    def create_snake(self):
        for number in POSITIONS:
            snake = Turtle(shape="square")
            self.snakes.append(snake)
            snake.color("white")
            snake.penup()
            snake.goto(number)

    def move(self):
        for number in range(len(self.snakes) - 1, 0, -1):
            # the snake replaced by the next snake, the last one to guide
            x = self.snakes[number - 1].xcor()
            y = self.snakes[number - 1].ycor()
            self.snakes[number].goto(x, y)
        self.snakes[0].forward(DISTANCE)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)
