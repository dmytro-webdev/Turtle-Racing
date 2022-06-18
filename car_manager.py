from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


def random_y():
    return random.randint(-250, 280)


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed_level = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1 or chance == 2:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.goto(300, random_y())
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.speed_level)

    def speed_up(self):
        self.speed_level += MOVE_INCREMENT



