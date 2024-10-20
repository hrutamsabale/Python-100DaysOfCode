# import colorgram
# from turtle import Turtle, Screen
# colors = colorgram.extract("image.jpeg", 15)
# color_palette = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_palette.append((r,g,b))
# print(color_palette)
import random
import turtle
from turtle import Turtle, Screen

colors_extracted = [(220, 149, 107), (140, 119, 8), (73, 127, 125), (14, 122, 175), (56, 10, 10), (78, 40, 65),
                    (185, 90, 156), (56, 165, 55), (226, 152, 223), (119, 8, 14), (4, 86, 120), (251, 251, 0)]
thala = Turtle()
turtle.colormode(255)
thala.hideturtle()
thala.speed("fastest")
thala.setheading(225)
thala.penup()
thala.forward(300)
thala.setheading(0)
thala.pendown()
for i in range(10):
    for j in range(10):
        thala.color(random.choice(colors_extracted))
        thala.begin_fill()
        thala.circle(10)
        thala.end_fill()
        thala.penup()
        thala.forward(50)
        thala.pendown()
    thala.penup()
    thala.right(180)
    thala.forward(500)
    thala.right(90)
    thala.forward(50)
    thala.right(90)
    thala.pendown()

my_screen = Screen()
my_screen.exitonclick()
