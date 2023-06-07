import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.title("U.S.A. States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

answer = screen.textinput(title="State name", prompt="Tell me a State")
print(answer)




screen.exitonclick()
