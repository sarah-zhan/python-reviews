# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# edge case test in Reeborg+World+Tests folder

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()

turn_left()

#follow the regular rule, turn right when you can, then go straight, turn left as your last resort
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()