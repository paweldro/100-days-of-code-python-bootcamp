import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(key="w", fun=snake.turn_up)
screen.onkey(key="s", fun=snake.turn_down)
screen.onkey(key="a", fun=snake.turn_left)
screen.onkey(key="d", fun=snake.turn_right)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.snake_body[-1].distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    if (snake.snake_body[-1].xcor() > 280 or snake.snake_body[-1].xcor() < -280 or snake.snake_body[-1].ycor() > 280
            or snake.snake_body[-1].ycor() < -280):
        score.game_over()
        game_is_on = False

    for segment in snake.snake_body[:-1]:
        if snake.snake_body[-1].distance(segment) < 10:
            score.game_over()
            game_is_on = False

screen.exitonclick()
