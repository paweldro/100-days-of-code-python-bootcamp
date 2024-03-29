import turtle
from turtle import Turtle, Screen
import random
import colorgram

t = Turtle()
turtle.colormode(255)
t.hideturtle()
t.speed("fastest")
rgb_colors = []
colors = colorgram.extract("dots.jpg", 30)
width = 10
dot = 30

t.penup()
t.left(90)
t.forward(dot*width)
t.left(90)
t.forward(dot*width)
t.setheading(0)
t.pendown()

for _ in range(width):
    for _ in range(width):
        t.pencolor(random.choice(colors).rgb)
        t.dot(dot)
        t.penup()
        t.forward(dot*2)
        t.pendown()
    t.penup()
    t.right(90)
    t.forward(dot*2)
    t.right(90)
    t.forward(width*(dot*2))
    t.right(180)
    t.pendown()

screen = Screen()
screen.exitonclick()
