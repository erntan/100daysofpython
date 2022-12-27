from turtle import Turtle

ALIGN = "center"
FONT = ("Futura", 18, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lscore = 0
        self.rscore = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()

    def  update_scoreboard(self):
        self.clear()
        self.write(f"{self.lscore} | {self.rscore}", align=ALIGN, font=FONT)
    def update_score(self, side):
        if side == 0:
            self.lscore += 1
        else:
            self.rscore +=1