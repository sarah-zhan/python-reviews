from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# create instance of menu
coffee_menu = Menu()
my_coffee = input(f"What would you like? ({coffee_menu.get_items()}) ")

# MyCoffeeMaker
my_coffee_maker = CoffeeMaker()
# MyMoneyMachine
my_money_machine = MoneyMachine()
# machine is on
is_on = True

while is_on:
    # print report
    if my_coffee == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    elif my_coffee not in (["latte", "espresso", "cappuccino"]):
        # check whether the choice is valid
        coffee_menu.find_drink(my_coffee.menu)
    else:
        # check resources sufficient
        if my_coffee_maker.is_resource_sufficient(my_coffee):
            my_money_machine.process_coins()
            my_money_machine.make_payment(cost)
