# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total = 0
count = 0
for number in student_heights:
  total += number
  count += 1
avg = round(total / count)
print(avg)


# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
max = 0
for score in student_scores:
  if (score > max):
    max = score

print(f'The highest score in the class is {max}')


#add even number
total = 0
for number in range(1, 101):
  if number % 2 == 0:
    total += number
print(f'The total even number is {total}')


# You are going to write a program that automatically prints the solution to the FizzBuzz game.

# Your program should print each number from 1 to 100 in turn.

# When the number is divisible by 3 then instead of printing the number it should print "Fizz".

# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

#   And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
# #Write your code below this row 👇

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)


#Password Generator Project
import random
from random import shuffle
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
#get letters
for n in range(0, nr_letters):
  random_letter_index = random.randint(0, len(letters) - 1)
  password.append(letters[random_letter_index])

#get numbers
for n in range(0, nr_numbers):
  random_number_index = random.randint(0, len(numbers) - 1)
  password.append(numbers[random_number_index])

#get symbols
for n in range(0, nr_symbols):
  random_symbol_index = random.randint(0, len(symbols) - 1)
  password.append(symbols[random_symbol_index])

#Eazy Level - Order not randomised:
print(''.join(password))

#Hard Level - Order of characters randomised:
shuffle(password)
print(''.join(password))