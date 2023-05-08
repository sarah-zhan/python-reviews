import random

random_integer = random.randint(1, 100) #include 1 and 100
print(random_integer)

random_float = random.random() #random number between 0 and 1, not included 1

random_float * 5 # random number 0 - 5, 5 not included

love_score = random.randint(1, 100)
print(f'Your love score is {love_score}')

#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲

#Write the rest of your code below this line 👇
random_coin = random.randint(0, 1)
if (random_coin == 0):
    print('Heads')
else:
    print('Tails')