from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto_start()
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def level_completed(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False

    def goto_start(self):
        self.goto(STARTING_POSITION)
