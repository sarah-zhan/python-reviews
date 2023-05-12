
import random
from hangman_art import stages, logo
from hangman_words import word_list

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = word_list[random.randint(0, 2)]  # or random.choice(world_list)
length = len(chosen_word)
#total lives
lives = 6
game_over = False

#starting with the logo
print(logo)
#Testing code
print(f'The solution is {chosen_word}.')

#create a list
display = []
#add '_'
for _ in range(length):
    display += '_'
#guess_list
guess_list = []
#while loop to check whether the word is the same
while not game_over:
    #Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess_letter = input('Guess of a letter: ').lower()
    guess_list.append(guess_letter)

    #check if it is duplicate
    if ''.join(guess_list).count(f'{guess_letter}') > 1:
        print(f"You've already guessed {guess_letter}" )

    #Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    for index in range(length):
        letter = chosen_word[index]
        if letter == guess_letter:
            display[index] = letter
    print(f'Guessed letter: {guess_letter}')
    print(display)
    print(stages[lives])

    if guess_letter not in list(chosen_word):
        lives -= 1
        print(f"You guess {guess_letter}, that's not in the word. You lose a life")
        print('------')
        print(stages[lives])
        if lives == 0:
          print('You lose.')
          game_over = True

    if '_' not in display:
        game_over = True
        print('You win.')
