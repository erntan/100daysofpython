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
            # Generate the body segments.
            segment = Turtle("square")
            segment.color("white")
            # segment.pencolor("black") # Outlines snek
            # Place the body segments.
            segment.penup()
            segment.goto(-STEP_SIZE * i, 0)
            self.segments.append(segment)
        self.head = self.segments[0]
        # Defining the movements
        def up():
            if self.head.heading() != DOWN:
                self.head.setheading(UP)

        def down():
            if self.head.heading() != UP:
                self.head.setheading(DOWN)

        def left():
            if self.head.heading() != RIGHT:
                self.head.setheading(LEFT)

        def right():
            if self.head.heading() != LEFT:
                self.head.setheading(RIGHT)

        self.mvmnts = {
            "Up": up,
            "Down": down,
            "Left": left,
            "Right": right,
        }

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)


# snek = mk_start_snk(3)
# while game_is_on:
#     screen.update()
#     time.sleep(.1)
#
#     for seg_num in range(len(snek) - 1, 0, -1):
#         new_x = snek[seg_num - 1].xcor()
#         new_y = snek[seg_num - 1].ycor()
#         snek[seg_num].goto(new_x, new_y)
#     snek[0].forward(20)
