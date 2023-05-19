from art import logo, vs
from data import data
import random
from replit import clear

#get random choice
def get_random_choice():
  return random.choice(data)


option_a = get_random_choice()
option_b = get_random_choice()
if option_a == option_b:
  option_b = random.choice(data)


#compare, return boolean
def compare(correct_answer, num1, num2):
  if num1 > num2:
    return correct_answer == 'a'
  elif num1 < num2:
    return correct_answer == 'b'


#game continue
game_continue = True
#game begin
print(logo)
#track the score
score = 0

while game_continue:

  option_a = option_b
  print(
    f"Compare A: {option_a['name']}, {option_a['description']}, from {option_a['country']}."
  )
  print(vs)
  option_b = random.choice(data)

  #if identical answer, need to make another choice
  while option_a == option_b:
    option_b = random.choice(data)

  print(
    f"Against B: {option_b['name']}, {option_b['description']}, from {option_b['country']}."
  )

  #ask user
  answer = input("Who has more followers? Type'A' or 'B': ").lower()

  #compare user answer and the correct answer
  is_correct = compare(answer, option_a['follower_count'],
                       option_b['follower_count'])

  clear()
  print(logo)
  
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}")
  else:
    print(f"Sorry, that's wrong. Final score: {score}")
    game_continue = False
