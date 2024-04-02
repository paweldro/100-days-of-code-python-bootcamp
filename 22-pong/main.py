import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_1 = Paddle(x=-350, y=0)
paddle_2 = Paddle(x=350, y=0)
ball = Ball(x=0, y=0)
score = Scoreboard()

screen.listen()
screen.onkey(key="w", fun=paddle_1.move_up)
screen.onkey(key="s", fun=paddle_1.move_down)
screen.onkey(key="Up", fun=paddle_2.move_up)
screen.onkey(key="Down", fun=paddle_2.move_down)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.ball_move()

    # Detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()

    # Detect collision with paddles
    if ball.distance(paddle_2) < 50 and ball.xcor() >= 330 or ball.distance(paddle_1) < 50 and ball.xcor() <= -330:
        ball.deflect()
        ball.move_speed *= 0.8

    # Detect collision with right wall
    if ball.xcor() >= 380:
        ball.refresh()
        score.increase_score_left()

    # Detect collision with left wall
    if ball.xcor() <= -380:
        ball.refresh()
        score.increase_score_right()

#screen.exitonclick()
