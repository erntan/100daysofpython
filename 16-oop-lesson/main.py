# from turtle import Turtle, Screen
#
# # Creating an object from a class
# timmy = Turtle()
# print(timmy)
#
# my_screen = Screen()
# print(my_screen.canvheight)     # Accessing an attribute
# my_screen.exitonclick()         # Accessing a method
#
# timmy.shape("turtle")
# timmy.color("chartreuse4")
# timmy.forward(100)


from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)