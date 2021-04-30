from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score_from_file()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score_to_file()
        self.score = 0

    def write_high_score_to_file(self):
        file = open("high_score.txt", "w")
        file.write(str(self.high_score))
        file.close()

    def read_high_score_from_file(self):
        file = open("high_score.txt", "r")
        high_score_storage = file.read()
        file.close()
        return int(high_score_storage)


    # def gamer_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

