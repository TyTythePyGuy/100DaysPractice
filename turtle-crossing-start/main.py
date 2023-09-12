import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
beanjima = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.onkey(beanjima.scoot, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.drive()
    if beanjima.next_level():
        beanjima.go_to_start()
        scoreboard.next_level()

    for cars in car.all_cars:
        if cars.distance(beanjima) < 20:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()
