from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 25, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"{self.score_left} : {self.score_right}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score_left(self):
        self.score_left += 1
        self.clear()
        self.update_scoreboard()

    def increase_score_right(self):
        self.score_right += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)
