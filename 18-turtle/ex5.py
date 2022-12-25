import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed(100)
########### Challenge 5 - Spirograph ########
num_circs = 10

for i in range(num_circs):
    angle = 360/num_circs * i
    tim.setheading(angle)
    tim.circle(50)

screen.exitonclick()
