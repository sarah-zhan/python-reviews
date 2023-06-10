import turtle
from turtle import Turtle, Screen
import pandas as pd
import os

screen = Screen()
screen.title("U.S.A. States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")


states_data = pd.read_csv("50_states.csv")
states_list = states_data.state.to_list()
states = states_data.state
score = 0
correct_answer = []

game_on = True

while game_on:

    answer = screen.textinput(title=f"{score}/50 States correct", prompt="Tell me a State").title()

    if answer == "Exit":
        # generate the missing list
        missing_answer = []
        for state in states_list:
            if state not in correct_answer:
                missing_answer.append(state)
        df = pd.DataFrame(missing_answer)
        df.to_csv("states_to_learn.csv")
        break
    # check whether the answer in the states list
    if answer in states_list and answer not in correct_answer:
        # if it is in the list, write the name
        pen = Turtle() # create a turtle
        pen.hideturtle()
        pen.penup()
        row_data = states_data[states_data.state == answer]
        pen.goto(int(row_data.x), int(row_data.y))
        pen.write(answer)
        score += 1
        correct_answer.append(answer)





