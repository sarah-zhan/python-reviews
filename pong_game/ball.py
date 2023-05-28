from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.x_move = 10
        self.y_move = 10


    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce(self):
        # move to the opposite
        self.y_move *= -1

    def catch(self):
        self.x_move *= -1

    def reset(self):
        self.home()
        self.catch()