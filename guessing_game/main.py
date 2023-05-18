# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

HARD_LEVEL = 5
EASY_LEVEL = 10

#target number generation
def generate():
  target = random.randint(1, 100)
  return target

#guess function
def guess():
  return int(input("Make a guess: "))

#compare numbers
def check_answer(guess_number, target_number):
  if guess_number > target_number:
    print("Too high.\n")
  elif guess_number < target_number:
    print("Too low.\n")
  else:
    print(f"You got it! Than answer was {guess_number}")

#set difficulty
def set_level():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == 'easy':
    return EASY_LEVEL
  else:
    return HARD_LEVEL

#game begin, show logo
print(logo)

def game():
  #welcome message
  print("Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100.  ")
  target_number = generate()
  print(f"sh....our answer is {target_number}")

  attempt = set_level()
  print(f"You have {attempt} attempts remaining to guess the number.")

  # if attempt < 0:
  #   print("You've run out of guesses, you lose")
  #   game_over = True

  guess_number = 0
  while guess_number != target_number:
    guess_number = guess()

    check_answer(guess_number, target_number)


game()

