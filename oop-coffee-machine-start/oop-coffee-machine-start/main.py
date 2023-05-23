from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# create instance of menu
coffee_menu = Menu()
my_coffee = input(f"What would you like? ({coffee_menu.get_items()})")

# check whether the choice is valid
coffee_menu.find_drink(my_coffee)
