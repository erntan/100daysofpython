#####Turtle Intro######

import turtle as t

timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.setheading(0)


######## Challenge 1 - Draw a Square ############
for i in range(4):
    timmy.forward(100)
    timmy.right(90)

screen = t.Screen()
screen.exitonclick()