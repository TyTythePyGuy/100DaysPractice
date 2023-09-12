from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.hideturtle()
        self.pu()
        self.goto(-220, 260)
        self.write(f"Level: {self.score+1}", align="center", font=FONT)

    def update_scoreboard(self):
        self.write(f"Level: {self.score+1}", align="center", font=FONT)

    def next_level(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER.\nFINAL SCORE: {self.score+1}", align="center", font=FONT)

