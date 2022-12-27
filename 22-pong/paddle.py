from turtle import Turtle
START_POS = [(350, 0), (-350,0)]
KEYS = [["Up", "Down"], ["w", "s"]]
STEP_SIZE = 20


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        # Set appearance
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5)
        self.penup()
        # Set orientation and position
        self.setheading(90)
        self.setpos(START_POS[pos])
        self.mvmnts = {
            KEYS[pos][0]: self.up,
            KEYS[pos][1]: self.down
        }

    def up(self):
        self.forward(STEP_SIZE)

    def down(self):
        self.backward(STEP_SIZE)