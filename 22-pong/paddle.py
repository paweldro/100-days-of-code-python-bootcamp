from turtle import Turtle

PADDLE_MOVE = 40


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(x, y)

    def move_up(self):
        if self.ycor() <= 250:
            pos_x = self.xcor()
            pos_y = self.ycor()
            self.goto(pos_x, pos_y + PADDLE_MOVE)

    def move_down(self):
        if self.ycor() >= -250:
            pos_x = self.xcor()
            pos_y = self.ycor()
            self.goto(pos_x, pos_y - PADDLE_MOVE)
