from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 11, "normal"))
        self.clear()
