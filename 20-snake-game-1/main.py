from turtle import Screen, Turtle
import time
from snek import Snek

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snek")

screen.tracer(0)
game_is_on = True


snek = Snek(3)
while game_is_on:
    screen.update()
    time.sleep(.1)

    snek.move()
    screen.listen()

    for key_press in snek.mvmnts:
        screen.onkeypress(key=key_press, fun=snek.mvmnts[key_press])

screen.exitonclick()
