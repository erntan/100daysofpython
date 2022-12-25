from turtle import Turtle, Screen
import random as rand

screen = Screen()
screen.setup(width=500, height=400)

# Generate racers
turtle_cols = ["red", "orange", "yellow", "green", "blue", "purple"]
racers = []
for col in turtle_cols:
    t = Turtle(shape="turtle")
    t.color(col)
    t.penup()
    racers.append(t)

# Set starting positions of racers
x_0 = -230
dist_from_racer = 20
num_racers = len(racers)


start_places = list(zip(racers,range(-180,180, round(360/len(turtle_cols)))))

for turtle, y in start_places:
    turtle.goto(-230, y)

usr_bet = screen.textinput(title="Make your bet.",prompt="Which color turtle will win the race?")

if usr_bet:
    race_on = True

while race_on:
    for racer in racers:
        if racer.xcor() > 230:
            winner = racer.pencolor()
            if winner == usr_bet:
                print("You won")
            else:
                print(f"You lost. The winner was {winner}")
            race_on = False
        rand_dist = rand.randint(0, 10)
        racer.forward(rand_dist)

screen.exitonclick()