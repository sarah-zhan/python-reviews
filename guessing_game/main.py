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
def check_answer(guess_number, target_number, rounds):
  if guess_number > target_number:
    print("Too high.")
    return rounds - 1
  elif guess_number < target_number:
    print("Too low.")
    return rounds - 1
  else:
    print(f"You got it! Than answer was {guess_number}")

#set difficulty
def set_level():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == 'easy':
    return EASY_LEVEL
  else:
    return HARD_LEVEL



def game():
  #game begin, show logo
  print(logo)
  #welcome message
  print("Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100.  ")
  target_number = generate()
  print(f"sh....our answer is {target_number}")

  rounds = set_level()

  guess_number = 0
  while guess_number != target_number:
    print(f"You have {rounds} attempts remaining to guess the number.")

    #guess a number
    guess_number = guess()

    #track the rounds
    rounds = check_answer(guess_number, target_number, rounds)
    if rounds == 0:
      print("You run out of attempts. Game over.")
      return

game()

