from data import *

revenue = 0
#make a choice
def make_a_choice():
  return input("What would you like to have, espresso, latte, or cappuccino?) ")

#calculate the money
def calculate_money(quarter, dime, nickle, penny):
  return 0.25 * quarter + 0.1 * dime + 0.05 * nickle + 0.01 * penny

#track resources
def check_ingredients(coffee):
  if coffee == "report":
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${revenue}")
  else:
    for ingredient in resources:
      resources[ingredient] -= MENU[coffee]["ingredients"][ingredient]
    return resources

#make coffee
def make_coffee():
  my_coffee = make_a_choice()

  #show report
  if my_coffee == 'report':
    check_ingredients(my_coffee)

  else:
    #check whether machine has enough resources
    for ingredient in MENU[my_coffee]['ingredients']:

      if MENU[my_coffee]['ingredients'][ingredient] > resources[ingredient]:
        print(f"There is not enough {ingredient}.")
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
          global revenue
          revenue += cost
          check_ingredients(my_coffee)
          make_coffee()
        else:
          print("Sorry, there is not enough money. Money refunded.")
          make_coffee()

make_coffee()