from turtle import Turtle
import random as rand

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.cars = []
        self.speed = 5

    def generate_car(self):
        yes = rand.randint(0, 5)
        if yes == 0:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(rand.choice(COLORS))
            car.setheading(180)
            car.setpos(320, rand.randrange(-250, 270, 22))
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.speed)
        self.cars = [car for car in self.cars if car.xcor() > -320]


    def increase_speed(self):
        self.speed += MOVE_INCREMENT


