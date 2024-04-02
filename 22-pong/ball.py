from turtle import Turtle

BALL_MOVE = 10


class Ball(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.penup()
        self.start_x = x
        self.start_y = y
        self.goto(self.start_x, self.start_y)
        self.ball_move_x = BALL_MOVE
        self.ball_move_y = BALL_MOVE
        self.move_speed = 0.1

    def ball_move(self):
        pos_x = self.xcor()
        pos_y = self.ycor()
        self.goto(pos_x + self.ball_move_x, pos_y + self.ball_move_y)

    def bounce(self):
        self.ball_move_y *= -1

    def deflect(self):
        self.ball_move_x *= -1

    def refresh(self):
        self.goto(self.start_x, self.start_y)
        self.ball_move_x *= -1
        self.ball_move_y = BALL_MOVE
        self.move_speed = 0.1
