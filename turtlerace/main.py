
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which Turtle Will Win The Race?:")
colors = ["red", "yellow", "blue", "green", "purple", "orange"]
y_pos = [-60,-30,0,30,60,90]
all_turtle = []


for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-200, y=y_pos[turtle_index])
    all_turtle.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won the game.{winning_color} is winner")
            else:
                print(f"You've lost the game.{winning_color} is winner")



        move_distance = random.randint(0, 10)
        turtle.forward(move_distance)


screen.exitonclick()