print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print('You can ride the rollercoaster!')
  age = int(input('What is your age?'))
  if age < 12:
     print('Please pay $5.')
  elif age <= 18:
     print('Please pay $7.')
  else:
     print('Please pay $12.')
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
bmi = weight / height **2

if bmi < 18.5:
   print('You are underweight.')
elif bmi < 25:
   print('You have a normal weight.')
elif bmi < 30:
   print('You are slightly overweight.')
elif bmi < 35:
   print('You are obese.')
else:
   print('You are clinically obese.')