from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color("white")
        self.ht()

    def win(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", font=("Courtier", 20, "normal"))
