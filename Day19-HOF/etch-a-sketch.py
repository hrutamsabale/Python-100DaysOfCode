from turtle import Turtle, Screen


def forward():
    thala.forward(10)


def reverse():
    thala.back(10)


def right():
    thala.right(10)


def left():
    thala.left(10)


def clear():
    thala.clear()
    thala.penup()
    thala.home()
    thala.pendown()


thala = Turtle()
my_screen = Screen()
my_screen.listen()
my_screen.onkey(key="w", fun=forward)
my_screen.onkey(key="s", fun=reverse)
my_screen.onkey(key="a", fun=left)
my_screen.onkey(key="d", fun=right)
my_screen.onkey(key="c", fun=clear)
my_screen.exitonclick()
