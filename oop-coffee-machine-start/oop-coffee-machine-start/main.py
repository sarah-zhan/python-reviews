from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# MyCoffeeMaker
my_coffee_maker = CoffeeMaker()
# MyMoneyMachine
my_money_machine = MoneyMachine()
# machine is on
is_on = True

while is_on:
    # create instance of menu
    coffee_menu = Menu()
    my_coffee = input(f"What would you like? ({coffee_menu.get_items()}) ")
    if my_coffee == "off":
        is_on = False
    # print report
    elif my_coffee == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        coffee = coffee_menu.find_drink(my_coffee)
        # check resources sufficient
        if my_coffee_maker.is_resource_sufficient(coffee):
            if my_money_machine.make_payment(coffee.cost):
                my_coffee_maker.make_coffee(coffee)
