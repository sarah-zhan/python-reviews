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

