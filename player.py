from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(0, -280)

    def go_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)

    def move_to_begin(self):
        self.goto(0, -280)

