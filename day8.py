def greet(name):
    print(f'Hello, welcome.{name}')
    print(f'How can I help you, {name}?')
    print(f'Tell me what do you want to do, {name}.')

greet()

def greet_with(name, location):
    print(f'Hello {name}')
    print(f'What is it like in {location}?')

#keyword arguments
greet_with(name='Jack', location='London')

#Write your code below this line 👇
import math
def paint_calc(height, width, cover):
    numbs = math.ceil(height * width / cover)
    print(f"You'll need {numbs} cans of paint.")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


#Write your code below this line 👇
def prime_checker(number):
    result_list = []
    for n in range(1, number + 1):
        result = number % n
        if result == 0:
            result_list.append(n)
    if len(result_list) == 2 and 1 in result_list and number in result_list:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)