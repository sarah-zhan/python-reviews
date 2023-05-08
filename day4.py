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
position_list = list(position)
row = int(position_list[1]) - 1
col_index = int(position_list[0]) - 1
map[row][col_index] = 'X'



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")