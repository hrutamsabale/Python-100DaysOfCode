from turtle import Turtle, Screen
from random import randint
colors = ["red", "orange", "yellow", "blue", "green", "black"]
turtle_objects = []
my_screen = Screen()
my_screen.setup(width=500, height=400)
y_cor = -180
for color in colors:
    new_turtle = Turtle("turtle")
    turtle_objects.append(new_turtle)
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-200, y=y_cor)
    y_cor += 60
to_continue = True
user_guess = my_screen.textinput("Guess kar!", "Kon jitega?")
while to_continue:
    for turtle in turtle_objects:
        if turtle.xcor() >= 200:
            to_continue = False
            if turtle.pencolor() == user_guess:
                print(f"You Won! {((turtle.pencolor()).capitalize())} won.")
            else:
                print(f"You lose.{((turtle.pencolor()).capitalize())} won.")
            break
        else:
            turtle.forward(randint(20,30))



