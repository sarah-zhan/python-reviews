from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.ht()
        self.goto(-50, 260)
        self.goto(30, 260)


    def l_win(self):
        self.l_score += 1
        self.clear()
        self.goto(-50, 260)
        self.write(self.l_score, font=("Courtier", 20, "normal"))

    def r_win(self):
        self.r_score += 1
        self.clear()
        self.goto(30, 260)
        self.write(self.r_score, font=("Courtier", 20, "normal"))