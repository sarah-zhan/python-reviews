from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.setposition(0, 280)
        self.score = 0
        # self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 11, "normal"))
        self.hideturtle()
        self.clear()
