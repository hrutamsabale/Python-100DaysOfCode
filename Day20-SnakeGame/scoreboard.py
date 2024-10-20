from turtle import Turtle

with open("data.txt") as file:
    HIGH_SCORE = int(file.read())


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = HIGH_SCORE
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=265)
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}, High Score: {self.high_score}", move=False, align='center', font=('Arial', 18, 'normal'))

    # def print_game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write(arg="Game Over!", move=False, align='center', font=('Arial', 24, 'normal'))

    def increase_score(self):
        self.score += 1

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))

    def reset(self):
        self.score = 0
        self.print_score()
