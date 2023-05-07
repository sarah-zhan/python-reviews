print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")


print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

print(len(input("What is your name? ")))

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
c = a
a = b
b = c



#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

print("Welcome to the Band Name Generator.")
city = input("What's name of the city you grew up in?\n")
pet_name = input("What is your pet's name?\n")
band_name = city + " " + pet_name
print("Your band name could be " + band_name)