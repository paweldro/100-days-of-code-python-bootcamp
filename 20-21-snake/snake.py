from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (20, 0), (40, 0)]
SQUARE = 20


class Snake:

    def __init__(self):
        self.snake_body = []

        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def turn_right(self):
        if self.snake_body[-1].heading() != 180:
            self.snake_body[-1].setheading(0)

    def turn_left(self):
        if self.snake_body[-1].heading() != 0:
            self.snake_body[-1].setheading(180)

    def turn_up(self):
        if self.snake_body[-1].heading() != 270:
            self.snake_body[-1].setheading(90)

    def turn_down(self):
        if self.snake_body[-1].heading() != 90:
            self.snake_body[-1].setheading(270)

    def move(self):
        for segment_number in range(len(self.snake_body) - 1):
            new_x = self.snake_body[segment_number + 1].xcor()
            new_y = self.snake_body[segment_number + 1].ycor()
            self.snake_body[segment_number].goto(new_x, new_y)
        self.snake_body[-1].forward(SQUARE)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.snake_body.append(new_segment)

    def extend(self):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(self.snake_body[0].position())
        self.snake_body.insert(0, new_segment)

    def reset(self):
        for segment in self.snake_body:
            segment.hideturtle()
            segment.clear()
        self.snake_body.clear()
        for position in STARTING_POSITIONS:
            self.add_segment(position)
