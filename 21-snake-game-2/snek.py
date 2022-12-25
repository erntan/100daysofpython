from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snek")

screen.tracer(0)
STEP_SIZE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snek:
    def __init__(self, len):
        self.len = len
        self.segments = []
        for i in range(len):
            self.add_segment((-STEP_SIZE * i, 0))
        self.head = self.segments[0]
        self.mvmnts = {
            "Up": self.up,
            "Down": self.down,
            "Left": self.left,
            "Right": self.right,
        }

    def add_segment(self, pos):
        # Generate the body segments.
        segment = Turtle("square")
        segment.color("white")
        # Place the body segments.
        segment.penup()
        segment.goto(pos)
        self.segments.append(segment)

    # Defining the movements
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x, new_y = self.segments[seg_num - 1].position()
            # new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def extend(self):
        self.add_segment(self.segments[-1].position())
