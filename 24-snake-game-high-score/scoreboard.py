from turtle import Turtle

ALIGN = "center"
FONT = ("Futura", 18, "bold")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.setpos(0, 270)
        self.font = FONT
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()