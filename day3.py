print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
  print('You can ride the rollercoaster!')
  age = int(input('What is your age?'))
  if age < 12:
     bill = 5
     print(f'Child tickets are ${bill}.')
  elif age <= 18:
     bill = 7
     print(f'Youth tickets are ${bill}.')
  elif (age >= 45 and age <= 55):
     bill = 0
     print(f'Mid age tickets are ${bill}.')
  else:
     bill = 12
     print(f'Adult tickets are ${bill}.')

  wants_photo = input('Do you want a photo taken? Y or N.')
  if (wants_photo == 'Y' or wants_photo =='y'):
     #add $3
     bill += 3

  print(f'Your total is ${bill}')

else:
  print('Sorry, you need to be taller.')


# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if (number % 2 == 0):
    print('This is an even number')
else:
    print('This is an odd number.')


# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / height ** 2)

if bmi < 18.5:
   print(f'Your bmi is {bmi}. You are underweight.')
elif bmi < 25:
   print(f'Your bmi is {bmi}. You have a normal weight.')
elif bmi < 30:
   print(f'Your bmi is {bmi}. You are slightly overweight.')
elif bmi < 35:
   print(f'Your bmi is {bmi}. You are obese.')
else:
   print(f'Your bmi is {bmi}. You are clinically obese.')


# on every year that is evenly divisible by 4

# **except** every year that is evenly divisible by 100

# **unless** the year is also evenly divisible by 400
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#check dive 4
if year % 4 == 0:
   #check divide 100
   if year % 100 == 0:
    #check divide 400
    if year % 400 == 0:
       print('Leap year.')
    else:
       print('Not leap year.')
   else:
    print('Leap year.')
else:
   print('Not leap year.')


# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == 'S':
   bill = 15
   if add_pepperoni == 'Y':
    bill += 2
elif size == 'M':
   bill = 20
   if add_pepperoni == 'Y':
    bill += 3
elif size == 'L':
   bill = 25
   if add_pepperoni == 'Y':
    bill += 3

if extra_cheese == 'Y':
   bill += 1

print(f'Your final bill is: ${bill}')


# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lower = name1.lower()
name2_lower = name2.lower()
true_total = name1_lower.count('t') + name1_lower.count('r') + name1_lower.count('u') + name1_lower.count('e') + name2_lower.count('t') + name2_lower.count('r') + name2_lower.count('u') + name2_lower.count('e')
love_total = name1_lower.count('l') + name1_lower.count('o') + name1_lower.count('v') + name1_lower.count('e') + name2_lower.count('l') + name2_lower.count('o') + name2_lower.count('v') + name2_lower.count('e')
love_score = int(str(true_total) + str(love_total))

if love_score < 10 or love_score > 90:
   print(f'Your score is {love_score}, you go together like coke and mentos.')
elif love_score >= 40 and love_score <= 50:
   print(f'Your score is {love_score}, you are alright together.')
else:
   print(f'Your score is {love_score}.')


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
option1 = input('You are at a crossroad, where do you want to go, left of right?\n ').lower()
if option1 == 'left':
   option2 = input('You have come to a lake. Do you want to swim or wait?\n ').lower()
   if option2 == 'wait':
      option3 = input('You are in front of 3 doors. Which door would you choose red, blue or yellow?\n ').lower()
      if option3 == 'red':
         print('Burned by fire. Game Over')
      elif option3 == 'yellow':
         print('You Win!')
      elif option3 == 'blue':
         print('Eaten by beasts. Game Over.')
      else:
         print('Game Over.')
   else:
      print('Attached by trout. Game Over.')
else:
   print('Fall into a hole. Game Over.')