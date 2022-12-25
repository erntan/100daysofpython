from turtle import Turtle, Screen
import random as rand
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('painting.jpg', 30)
#
# for color in colors:
#     rgb_colors.append(color.rgb)
#
# color_tups = [(c.r, c.g, c.b) for c in rgb_colors]

color_list = [(226, 231, 236), (58, 106, 148), (224, 200, 109), (134, 84, 58), (223, 138, 62),
              (196, 145, 171), (234, 226, 204), (224, 234, 230), (141, 178, 204), (139, 82, 105),
              (209, 90, 69), (188, 80, 120), (68, 105, 90), (237, 225, 233), (134, 182, 136),
              (133, 133, 74), (63, 156, 92), (48, 156, 194), (183, 192, 201), (214, 177, 191),
              (19, 57, 93), (21, 68, 113), (112, 123, 149), (229, 174, 165), (172, 203, 182),
              (158, 205, 215), (69, 58, 47), (108, 47, 60), (53, 70, 65), (72, 64, 53)]

dot_size = 20
t = Turtle()
screen = Screen()
screen.colormode(255)

canvas = 400
num_xdots = 10
num_ydots = 10

xdist = canvas/num_xdots
ydist = canvas/num_ydots

offset = -100
for i in range(num_ydots):
    for j in range(num_xdots):
        t.penup()
        t.setpos(xdist*j + offset,ydist*i + offset)
        t.pendown()
        t.pencolor(rand.choice(color_list))
        t.dot(dot_size)

screen.exitonclick()

