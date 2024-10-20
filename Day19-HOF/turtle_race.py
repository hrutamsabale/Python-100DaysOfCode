from turtle import Turtle, Screen
import random


def turtle_color(turtle_object):
    return (turtle_object.color())[0]


def make_lines():
    line_maker = Turtle()
    line_maker.hideturtle()
    line_maker.speed("fastest")
    line_maker.penup()
    line_maker.goto(x=-200, y=180)
    line_maker.pendown()
    line_maker.goto(x=-200, y=-180)
    line_maker.penup()
    line_maker.goto(x=200, y=180)
    line_maker.pendown()
    line_maker.goto(x=200, y=-180)


def has_won():
    for turtle in turtle_objects:
        if turtle.xcor() >= 200:
            global winning_turtle
            winning_turtle = turtle_color(turtle)
            return True

    return False


def random_movement():
    for turtle in turtle_objects:
        forward_dist = random.randint(10, 30)
        turtle.forward(forward_dist)


colors = ["red", "blue", "green", "black", "purple", "yellow"]
winning_turtle = ""
turtle_objects = []
my_screen = Screen()
my_screen.setup(width=500, height=400)
user_choice = (my_screen.textinput("Make a bet!", "Who do you think will win?")).lower()
y_axis = -150
for color in colors:
    new_turtle = Turtle("turtle")
    turtle_objects.append(new_turtle)
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-200, y=y_axis)
    y_axis += 50
make_lines()
while not has_won():
    random_movement()
if winning_turtle == user_choice:
    print(f"You win! {winning_turtle.capitalize()} won the race.")
else:
    print(f"You lost! {winning_turtle.capitalize()} won the race.")

