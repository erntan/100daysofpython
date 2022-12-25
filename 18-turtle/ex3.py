import turtle as t
from random import randint

tim = t.Turtle()
screen = t.Screen()
screen.colormode(255)
########### Challenge 3 - Draw Shapes ########
len_side = 100
num_sides = range(4, 10)

tim.penup()
tim.right(90)
tim.forward(50)
tim.right(90)
tim.forward(50)
tim.right(180)
tim.pendown()
for sides in num_sides:
    angle = 360 / sides
    tim.pencolor(randint(0,255),randint(0,255),randint(0,255))
    for i in range(sides):
        tim.forward(len_side)
        tim.left(angle)



screen.exitonclick()

