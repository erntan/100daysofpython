from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Game screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
# screen.tracer(delay=2)    # Turns off animation

screen.tracer(0)
scoreboard = Scoreboard()
paddle_r = Paddle(0)
paddle_l = Paddle(1)
b = Ball()

game_is_on = True
screen.listen()
while game_is_on:
    screen.update()
    for key in paddle_r.mvmnts:
        screen.onkeypress(key=key, fun=paddle_r.mvmnts[key])

    for key in paddle_l.mvmnts:
        screen.onkeypress(key=key, fun=paddle_l.mvmnts[key])

    # Detect collision with walls
    if 300 - abs(b.ycor()) < 15:
        b.setheading(-b.heading())

    # Detect collision with paddles
    if (b.distance(paddle_r.pos()) < 50 and b.xcor() > 320) or (b.distance(paddle_l.pos()) < 50 and b.xcor() > -320):
        b.setheading(-b.heading() + 90)

    # Detect goal
    if abs(b.xcor()) > 380:
        b.setheading(b.heading() + 180)
        if b.xcor() > 0:
            scoreboard.update_score(0)
            scoreboard.update_scoreboard()
        if b.xcor() < 0:
            scoreboard.update_score(1)
            scoreboard.update_scoreboard()

        b.goto(0,0)

    b.forward(.2)


screen.exitonclick()
