
#Step 1
import random
word_list = ["aardvark", "baboon", "camel"]

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = word_list[random.randint(0, 2)]  # or random.choice(world_list)

#Testing code
print(f'The solution is {chosen_word}.')

#Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess_letter = input('Guess of a letter: ').lower()

#create a list
display = []
#Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in chosen_word:
    if letter == guess_letter:
        display.append(letter)
    else:
        display.append('_')