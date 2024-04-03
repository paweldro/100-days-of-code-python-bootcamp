import random
import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()
cars = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(key="w", fun=tim.turtle_move)

game_is_on = True
car_counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move_cars()
    car_counter += 1
    if car_counter >= 6:
        cars.generate_car()
        car_counter = 0

    for car in cars.all_cars:
        if tim.distance(car) <= 20:
            tim.turtle_refresh()
            score.game_over()
            game_is_on = False
    if tim.turtle_finish():
        cars.cars_speedup()
        score.increase_score()

turtle.exitonclick()