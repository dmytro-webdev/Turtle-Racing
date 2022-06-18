
from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from score_board import ScoreBoard

import threading
WIDTH = 600
HEIGHT = 600
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.title('Turtle Racing')
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = ScoreBoard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.2)
    car_manager.create_car()
    car_manager.move()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            score_board.game_over()
            is_game_on = False

        if player.ycor() > 290:
            player.move_to_begin()
            score_board.update_level()
            car_manager.speed_up()
screen.exitonclick()