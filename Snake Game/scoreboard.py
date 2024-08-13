from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.extract_highest_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.updating_highest_score()
        self.score = 0
        self.update_scoreboard()


    def increase_score(self):

        self.score += 1
        self.update_scoreboard()

    def extract_highest_score(self):
        with open("data.txt") as data_file:
            highest_score = int(data_file.read())
            return highest_score

    def updating_highest_score(self):
        with open("data.txt", mode="w") as data_file:
            data_file.write(str(self.high_score))


