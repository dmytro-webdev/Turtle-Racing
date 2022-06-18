from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed_level = 1
        self.hideturtle()
        self.penup()
        self.goto(-290, 250)
        self.write(f"level: {self.speed_level}", False, align='left', font=("Coruier", 18, "italic"))

    def update_level(self):
        self.clear()
        self.speed_level += 1
        self.write(f"level: {self.speed_level}", False, align='left', font=("Coruier", 18, "italic"))

    def game_over(self):
        self.hideturtle()
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=("Coruier", 20, "normal"))