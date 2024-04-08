import random
import pandas
import time
from turtle import Turtle, Screen

screen_width = 725
screen_height = 491
screen = Screen()
screen.setup(width=screen_width, height=screen_height)
screen.bgpic("blank_states_img.gif")
t = Turtle()
t.penup()
t.hideturtle()

state_data = pandas.read_csv("50_states.csv")
guessed_state = []
all_states = state_data.state.to_list()
missing_states = []
while len(guessed_state) < 50:
    user_state = screen.textinput(title=f"{len(guessed_state)}/50", prompt="Enter state: ")

    if user_state.lower() == "exit":
        missing_states = [state for state in all_states if state not in guessed_state]
        missing_states_dataframe = pandas.DataFrame(missing_states)
        missing_states_dataframe.to_csv("missing_states.csv")
        break

    for s in state_data.state:
        if user_state.lower() == s.lower():
            state_tup = (state_data[state_data.state == s].x.item(), state_data[state_data.state == s].y.item())
            if s not in guessed_state:
                guessed_state.append(s)
            t.goto(state_tup)
            t.write(arg=s, move=False, font=('Arial', 8, 'normal'))
            time.sleep(1)



screen.exitonclick()
