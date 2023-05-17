from art import logo
from replit import clear
import random



game_play = input("Do you want to play a game of Blackjack? Type 'y' to start the game or 'n' to exit: ")

def deal_card():
    '''return a random card'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    '''calculate the total of the cards'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)



  # print(logo)
  #pick 2 cards for player, show total score, consider they have the same probability to be drawn
user_cards = []
computer_cards = []
game_over = False
for _ in range(0, 2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while not game_over:
  #while loop to repeat the game, until the user end the game
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)

  print(f'Your cards: {user_cards}, current score: {calculate_score(user_cards)}')
  print(f'Computer first card: {computer_cards[0]}')

  if user_score == 0 or computer_score == 0 or user_score > 21:
    game_over = True
  else:
    get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if get_another_card == 'y':
      user_cards.append(deal_card())
    else:
      game_over = True





