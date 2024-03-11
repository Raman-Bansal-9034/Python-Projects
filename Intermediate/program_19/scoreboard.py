# Score board used in our program is also going to a turtle.So we will use write method from our turtle module
# to create a score board.

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()  # To clear the previous score board and create and display new score board.
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f" Score : {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
