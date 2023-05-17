from art import logo
from replit import clear
import random
game = True


game_play = input("Do you want to play a game of Blackjack? Type 'y' to start the game or 'n' to exit: ")

def deal_card():
    '''return a random card'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    if sum(cards) == 0 or sum(cards) > 21:
        game_over = True
    return sum(cards)

while game:

  print(logo)
  #pick 2 cards for player, show total score, consider they have the same probability to be drawn
  user_cards = []
  computer_cards = []
  for _ in range(0, 2):
      user_cards.append(deal_card())
      computer_cards.append(deal_card())

  print(f'Your cards: {user_cards}, current score: {calculate_score(user_cards)}')
  print(f'Computer first card: {computer_cards[0]}')


  


