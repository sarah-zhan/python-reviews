# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
print(int(two_digit_number[0]) + int(two_digit_number[1]))

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = float(weight) /  (float(height) * float(height))
print(int(BMI))

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
years = 90 - int(age)
months = years * 12
weeks = years * 52
days = years * 365

print(f'You have {days} days, {weeks} weeks, and {months} months left.')