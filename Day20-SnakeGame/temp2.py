from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(key="Up", fun=snake.go_north)
screen.onkey(key="Down", fun=snake.go_south)
screen.onkey(key="Left", fun=snake.go_west)
screen.onkey(key="Right", fun=snake.go_east)
to_continue = True
while to_continue:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        scoreboard.print_score()
        food.move_to_random_location()
        snake.extend()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # to_continue = False
        # scoreboard.print_game_over()
        scoreboard.update_high_score()
        scoreboard.reset()
        snake.reset()
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            # to_continue = False
            # scoreboard.print_game_over()
            scoreboard.update_high_score()
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
