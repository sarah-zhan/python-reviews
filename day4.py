import random

# random_integer = random.randint(1, 100) #include 1 and 100
# print(random_integer)

# random_float = random.random() #random number between 0 and 1, not included 1

# random_float * 5 # random number 0 - 5, 5 not included

# love_score = random.randint(1, 100)
# print(f'Your love score is {love_score}')

#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲

#Write the rest of your code below this line 👇
# random_coin = random.randint(0, 1)
# if (random_coin == 0):
#     print('Heads')
# else:
#     print('Tails')

#append one item, extend a list

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
selected_index = random.randint(0, len(names) - 1)
selected_person = names[selected_index] #random.choice(names)
print(f'{selected_person} is going to buy the meal today!')


# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
row = int(position[1]) - 1
col_index = int(position[0]) - 1
map[row][col_index] = 'X'



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


# Start the game by asking the player:

# "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

# From there you will need to figure out:

# How you will store the user's input.
# How you will generate a random choice for the computer.
# How you will compare the user's and the computer's choice to determine the winner (or a draw).
# And also how you will give feedback to the player.

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choice_human = input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n')
choice_computer = random.randint(0, 2)

if int(choice_human) == 0:
    if choice_computer == 2:
        print(f'Your choice is Rock\n{rock}')
        print(f'Computer choice is Scissors\n{scissors}')
        print('You win.')
    elif choice_computer == 1:
        print(f'Your choice is Rock\n{rock}')
        print(f'Computer choice is Paper\n{paper}')
        print('You lose.')
    else:
        print(f'Both are {rock}\nIt is a tie.')
elif int(choice_human) == 1:
    if choice_computer == 2:
        print(f'Your choice is Paper\n{paper}')
        print(f'Computer choice is Scissors\n{scissors}')
        print('You lose.')
    elif choice_computer == 0:
        print(f'Your choice is Paper\n{paper}')
        print(f'Computer choice is Rock\n{rock}')
        print('You win.')
    else:
        print(f'Both are {paper}\nIt is a tie.')
elif int(choice_human) == 2:
    if choice_computer == 1:
        print(f'Your choice is Scissors\n{scissors}')
        print(f'Computer choice is Paper\n{paper}')
        print('You win.')
    elif choice_computer == 0:
        print(f'Your choice is Scissors\n{scissors}')
        print(f'Computer choice is Rock\n{rock}')
        print('You lose.')
    else:
        print(f'Both are {scissors}\nIt is a tie.')