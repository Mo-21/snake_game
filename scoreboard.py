from turtle import Turtle


def get_high_score():
    with open("highscore.txt") as file:
        hs = file.read()
        return int(hs) if hs else 0


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.score = 0
        self.high_score = get_high_score()
        self.update_score()

    def update_score(self):
        self.clear()
        self.set_high_score()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def set_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score

    def write_high_score(self):
        with open("highscore.txt", mode="w") as files:
            files.write(f"{self.high_score}")

    def game_over(self):
        self.score = 0
        self.write_high_score()
        self.update_score()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 24, "normal"))
