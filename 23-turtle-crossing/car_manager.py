from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_LINE = 300


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def generate_car(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.penup()
        car.goto(STARTING_LINE, random.randint(-250, 290))
        self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.goto(car.xcor() - self.move_distance, car.ycor())
            if car.xcor() <= -320:
                car.hideturtle()
                car.clear()
                self.all_cars.remove(car)

    def cars_speedup(self):
        self.move_distance += MOVE_INCREMENT
