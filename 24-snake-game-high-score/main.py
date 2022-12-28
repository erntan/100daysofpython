from turtle import Screen
import time
from snek import Snek
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snek")

screen.tracer(0)
game_is_on = True


snek = Snek(3)
food = Food()
scoreboard = Scoreboard()

while game_is_on:
    screen.update()
    time.sleep(.1)

    snek.move()
    screen.listen()

    for key_press in snek.mvmnts:
        screen.onkeypress(key=key_press, fun=snek.mvmnts[key_press])

    # Detect collision with food
    if snek.head.distance(food) < 15:
        food.refresh()
        snek.extend()
        scoreboard.update_score()

    # Detect collision with wall
    if snek.head.xcor() > 280 or snek.head.xcor() < -280 or snek.head.ycor() < -280 or snek.head.ycor() > 280:
        # game_is_on = False
        scoreboard.reset()
        snek.reset()

    # Detect collision with tail
    for segment in snek.segments[1:]:
        if snek.head.distance(segment) < 10:
            # game_is_on = False
            scoreboard.reset()
            snek.reset()

screen.exitonclick()
