import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Initialize the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

FINISH_LINE_Y = 280
scoreboard = Scoreboard()
car_manager = CarManager()

# Initialize the player
player = Player()

game_is_on = True
screen.listen()
while game_is_on:
    time.sleep(0.1)
    screen.update()

    screen.onkeypress(player.move, "Up") # Move when key pressed
    # Player hits a car
    cars_in_path = [car for car in car_manager.cars if abs(car.xcor()) <= 10 and
                    abs(player.ycor() - car.ycor()) <= 20]
    if len(cars_in_path) != 0:
        scoreboard.game_over()
        game_is_on = False


    # Player reaches top of screen
    if player.ycor() >= FINISH_LINE_Y:
        # Increase level
        scoreboard.update_level()
        scoreboard.update_scoreboard()
        car_manager.increase_speed()
        # Reset player
        player.reset()

    car_manager.generate_car()
    car_manager.move_cars()

screen.exitonclick()