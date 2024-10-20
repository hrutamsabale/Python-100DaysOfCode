from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
NORTH = 90
SOUTH = 270
WEST = 180
EAST = 0


class Snake:
    def __init__(self):
        self.snake_segments = []
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        self.head = self.snake_segments[0]
        self.head.color("red")

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.snake_segments.append(new_segment)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

    def move(self):
        for i in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[i - 1].xcor()
            new_y = self.snake_segments[i - 1].ycor()
            self.snake_segments[i].goto(x=new_x, y=new_y)
        self.head.forward(20)

    def go_west(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)

    def go_east(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)

    def go_south(self):
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)

    def go_north(self):
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)

    def reset(self):
        for segment in self.snake_segments:
            segment.goto(5000, 5000)
        self.snake_segments.clear()
        self.__init__()



