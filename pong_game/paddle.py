from turtle import Turtle

STARTING_POSITION = [(350, 0)]
UP = 90
DOWN = 270
MOVEMENT = 20
PADDLE_HEIGHT = 100
PADDLE_WIDTH = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.pu()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + MOVEMENT
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - MOVEMENT
        self.goto(self.xcor(), new_y)
