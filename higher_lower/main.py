from art import logo, vs
from data import data
import random

#choose A function
# def choose_a():
#   option_a = random.choice(data)
#   return f"Compare A: {option_a['name']}, {option_a['description']}, from {option_a['country']}."

#choose B function
# def choose_b():
#   option_b = random.choice(data)
#   return f"Against B: {option_b['name']}, {option_b['description']}, from {option_b['country']}."

#compare
def compare(num1, num2):
  if num1 > num2:
    return 'A'
  elif num1 < num2:
    return 'B'



#game begin
print(logo)

option_a = random.choice(data)
option_b = random.choice(data)

def game_continue():
  print(f"Compare A: {option_a['name']}, {option_a['description']}, from {option_a['country']}.")
  print(vs)
  print(f"Against B: {option_b['name']}, {option_b['description']}, from {option_b['country']}.")

#ask user
answer = input("Who has more followers? Type'A' or 'B': ")

#track the score
score = 0

#compare user answer and the truth
if compare(option_a['follower_count'], option_b['follower_count']) == answer:
  score += 1
  print(f"You're right! Current score: {score}")
  option_a = option_b
  game_continue()
else:
  print(f"Sorry, that's wrong. Final score: {score}")