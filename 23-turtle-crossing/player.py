from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.left(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def turtle_move(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def turtle_refresh(self):
        self.goto(STARTING_POSITION)

    def turtle_finish(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.turtle_refresh()
            return True
        return False
