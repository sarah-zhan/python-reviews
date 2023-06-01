from turtle import Turtle




class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.setposition(0, 270)
        self.score = 0
        with open("data.txt", mode="r") as data:
            data_score = data.read()
        self.highest_score = int(data_score)
        self.hideturtle()
        self.clear()
        self.write(f"Score: {self.score} Highest Score: {self.highest_score} ",
                   align="center", font=("Courier", 20, "normal"))

    # def game_over(self):
    #     self.penup()
    #     self.goto(-130, 0)
    #     self.write("😔 Game Over 😔", font=("Courier", 24, "normal"))

    def update_score(self):
        # clear the record
        self.clear()
        # update the score
        self.score += 1
        # show the scoreboard again
        self.write(f"Score: {self.score} Highest Score: {self.highest_score} ",
                   align="center", font=("Courier", 20, "normal"))
        with open("data.txt", mode="r+") as data:
            data.write(str(self.highest_score))

    def update_highest_score(self):
        if int(float(self.score)) > int(float(self.highest_score)):
            self.highest_score = self.score
        self.score = 0
        self.update_score()
