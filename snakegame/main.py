from turtle import Screen
from snake_body import Snake
from snake_food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Floopy")
screen.tracer(0)

floopy = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(floopy.up, "Up")
screen.onkey(floopy.down, "Down")
screen.onkey(floopy.left, "Left")
screen.onkey(floopy.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    floopy.move()

    #detects collision with food
    if floopy.head.distance(food) < 15:
        floopy.extend()
        food.refresh()
        scoreboard.increase_score()

    #detects collision with wall
    if floopy.head.xcor() > 290 or floopy.head.xcor() < -290 or floopy.head.ycor() > 300 or floopy.head.ycor() < -290:
        scoreboard.reset()
        floopy.reset()

    #detect collision with tail
    for segments in floopy.snake_body[1:]:
        if floopy.head.distance(segments) < 10:
            scoreboard.reset()
            floopy.reset()


screen.exitonclick()