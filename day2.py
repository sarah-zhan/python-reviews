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

#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print('welcome to the tip calculator')
total = float(input('what is the total bill before tip? $'))
people = int(input('how many people to split the bill? '))
tip = float(input('how many tip to pay 10, 12, or 15 ')) * 0.01
pay_by_person = (total / people) * (1 + tip)
print(f'Everyone pay {pay_by_person:.2f}')