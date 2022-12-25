import turtle
import turtle as t
import random as rand

tim = t.Turtle()
screen = t.Screen()
########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
dirs = [0, 90, 180, 270]

distance = 20
steps = 40

screen.colormode("rgb")

# thicker lines
tim.width(20)
tim.speed(10)
# Faster turtle

for i in range(steps):
    dir = rand.choice(dirs)
    col = rand.choice(colours)
    tim.pencolor(col)
    tim.setheading(dir)
    tim.forward(steps)

screen.exitonclick()
