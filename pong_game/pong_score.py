from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 50, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(0, 230)
        self.update_score()

    def update_score(self):
        self.write(f"{self.l_score}    {self.r_score}", align=ALIGNMENT, font=FONT)

    def increase_score_l(self):
        self.l_score += 1
        self.clear()
        self.update_score()

    def increase_score_r(self):
        self.r_score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        if self.l_score == 10:
           print("Game Over, Left player wins!")
        if self.r_score == 10:
            print("Game Over, Right player wins!")