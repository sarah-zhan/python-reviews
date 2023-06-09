import turtle
from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title("U.S.A. States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

answer = screen.textinput(title="State name", prompt="Tell me a State").title()
states_data = pd.read_csv("50_states.csv")
states_list = states_data.state.to_list()
states = states_data.state

# check whether the answer in the states list
if answer in states_list:
    # if it is in the list, write the name
    pen = Turtle() # create a turtle
    pen.hideturtle()
    pen.penup()
    row_data = states_data[states_data.state == answer]
    pen.goto(int(row_data.x), int(row_data.y))
    pen.write(answer)



screen.exitonclick()
