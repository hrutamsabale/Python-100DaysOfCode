from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

R_PADDLE_POS = (350, 0)
L_PADDLE_POS = (-350, 0)
SLEEP_TIME = 0.05

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=800, height=600)
my_screen.tracer(0)
my_screen.listen()

r_paddle = Paddle(R_PADDLE_POS)
l_paddle = Paddle(L_PADDLE_POS)
ball = Ball()
scoreboard = Scoreboard()

to_continue = True
while to_continue:
    scoreboard.write_scores()
    my_screen.update()
    ball.move()
    sleep(SLEEP_TIME)
    my_screen.onkey(key="Up", fun=r_paddle.move_up)
    my_screen.onkey(key="Down", fun=r_paddle.move_down)
    my_screen.onkey(key="w", fun=l_paddle.move_up)
    my_screen.onkey(key="s", fun=l_paddle.move_down)
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce("y")
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) or (ball.distance(l_paddle) < 50 and ball.xcor() < -330):
        ball.bounce("x")
        SLEEP_TIME /= 1.25
    if ball.xcor() >= 390:
        ball.reset()
        SLEEP_TIME = 0.05
        scoreboard.l_score += 1
    if ball.xcor() <= -390:
        ball.reset()
        SLEEP_TIME = 0.05
        scoreboard.r_score += 1



my_screen.exitonclick()