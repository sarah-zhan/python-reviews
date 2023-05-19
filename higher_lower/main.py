from art import logo, vs
from data import data
import random

#choose A function
def choose_a():
  option_a = random.choice(data)
  return f"Compare A: {option_a['name']}, {option_a['description']}, from {option_a['country']}."

#choose B function
def choose_b():
  option_b = random.choice(data)
  return f"Against B: {option_b['name']}, {option_b['description']}, from {option_b['country']}."

#compare
def compare(num1, num2):
  if num1 > num2:
    return 'A'
  elif num1 < num2:
    return 'B'

