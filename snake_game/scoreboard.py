from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.setposition(0, 270)
        self.score = 0
        self.hideturtle()
        self.clear()

    def game_over(self):
        self.penup()
        self.goto(-100, 0)
        self.write("Game Over", font=("Courier", 24, "normal"))