from art import logo, vs
from data import data
import random

#get random choice
option_a = random.choice(data)
option_b = random.choice(data)
if option_a == option_b:
  option_b = random.choice(data)

#compare
def compare(num1, num2):
  if num1 > num2:
    return 'A'
  elif num1 < num2:
    return 'B'

#check answer
def check_answer(answer, correct_answer, score):
  if answer == correct_answer:
    score += 1
    print(f"You're right! Current score: {score}")
    option_a = option_b
    print(f"Compare A: {option_a['name']}, {option_a['description']}, from {option_a['country']}.")
    print(vs)
    option_b = random.choice(data)
    if option_a == option_b:
      option_b = random.choice(data)
    print(f"Against B: {option_b['name']}, {option_b['description']}, from {option_b['country']}.")
    answer = input("Who has more followers? Type'A' or 'B': ")
  else:
    print(f"Sorry, that's wrong. Final score: {score}")


#game begin
print(logo)

print(f"Compare A: {option_a['name']}, {option_a['description']}, from {option_a['country']}.")
print(vs)
print(f"Against B: {option_b['name']}, {option_b['description']}, from {option_b['country']}.")

#ask user
answer = input("Who has more followers? Type'A' or 'B': ")

#track the score
score = 0

#compare user answer and the correct answer
correct_answer = compare(option_a['follower_count'], option_b['follower_count'])
check_answer(answer, correct_answer, score)