import random
from turtle import Turtle, Screen

screen_width = 500
screen_height = 400
screen = Screen()
screen.setup(width=screen_width, height=screen_height)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "blue", "purple"]
turtles = []

start_x = -1 * (screen_width / 2) + 10
start_y = (len(colors) * 50) / 2

for color in colors:
    tim = Turtle(shape="turtle")
    tim.color(color)
    tim.penup()
    tim.goto(x=start_x, y=start_y)
    start_y -= 50
    turtles.append(tim)
    tim.pendown()

turtle_win = False
while True:
    for turtle in turtles:
        turtle.penup()
        turtle_move = random.randint(0, 10)
        turtle.setx(turtle.pos()[0] + turtle_move)
        turtle.pendown()
        if turtle.pos()[0] > (screen_width / 2) - 20:
            winner = turtle.color()
            if winner[0] == user_bet.lower():
                print(f"You've won! The {winner[0]} turtle is the winner!")
            else:
                print(f"You've lose! The {winner[0]} turtle is the winner!")
            turtle_win = True
            break
    if turtle_win:
        break

screen.exitonclick()
