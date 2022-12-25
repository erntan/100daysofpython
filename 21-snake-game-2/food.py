from turtle import Turtle
import random as rand

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("blue")
        self.speed("fastest")
        self.goto(rand.randint(-280, 280), rand.randint(-280, 280))

    def refresh(self):
        self.goto(rand.randint(-280, 280), rand.randint(-280, 280))