from data import *

#make a choice
def make_a_choice():
  return input("What would you like to have, espresso, latte, or cappuccino?) ")

#calculate the money
def calculate_money(quarter, dime, nickle, penny):
  return 0.25 * quarter + 0.1 * dime + 0.05 * nickle + 0.01 * penny

def make_coffee():
  my_coffee = make_a_choice()

  #check resource
  water = resources["water"] - MENU[my_coffee]["ingredients"]["water"]
  milk = resources["milk"] - MENU[my_coffee]["ingredients"]["milk"]
  coffee = resources["coffee"] - MENU[my_coffee]["ingredients"]["coffee"]

  #show report
  if my_coffee == 'report':
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g")

  #check whether machine has enough resources
  if water < 0:
    print("There is not enough water.")
    make_coffee()
  elif milk < 0:
    print("There is not enough milk.")
    make_coffee()
  elif coffee < 0:
    print("There is not enough coffee.")
    make_coffee()
  else:
    print("Please insert coins.")
    quarter = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickle = int(input("How many nickles?: "))
    penny = int(input("How many pennies?: "))
    total = calculate_money(quarter, dime, nickle, penny)
    cost = MENU[my_coffee]["cost"]
    if total >= cost:
      change = round(total - cost, 2)
      print(f"Here is ${change} in change.")
      print(f"Here is your {my_coffee} ☕. Enjoy!")
      make_coffee()
    else:
      print("Sorry, there is not enough money. Money refunded.")
      make_coffee()

make_coffee()