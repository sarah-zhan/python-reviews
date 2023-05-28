from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.write({self.score}, align="center", font=("Courtier", 20, "normal"))

    def win(self):
        self.score += 1
