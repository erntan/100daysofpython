import turtle as t

tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########

for i in range(100):
    if i % 2 == 0:
        tim.pendown()
    else:
        tim.penup()
    tim.forward(6)
