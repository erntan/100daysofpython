from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
machine_on = True

while machine_on:
    order = input("What would you like? (espresso/latte/cappuccino)")
    if order == "off":
        print("Goodbye.")
        machine_on = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        coffee = menu.find_drink(order)
        paid = money_machine.make_payment(coffee.cost)
        if paid and coffee_maker.is_resource_sufficient(coffee):
            coffee_maker.make_coffee(coffee)