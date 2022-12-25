from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def counterclockw():
    tim.left(10)

def clockw():
    tim.right(10)

mvmnts = {
    "w": move_forwards,
    "s": move_backward,
    "a": counterclockw,
    "d": clockw,
    "c": tim.clear
}
screen.listen()

for key_press in mvmnts:
    screen.onkeypress(key=key_press, fun=mvmnts[key_press])

screen.exitonclick()

# TODO w = forward
# TODO s = backward
# TODO a = counter clockwise
# TODO d = clockwise
# TODO c = clear