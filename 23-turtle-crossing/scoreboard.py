from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.setpos(-280,260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level {self.level}", align="left", font=FONT)

    def update_level(self):
        self.level += 1

    def game_over(self):
        self.setpos(0,0)
        self.write("GAME OVER", align="center", font=FONT)
