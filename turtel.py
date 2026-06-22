
from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()

screen.setup(width=500, height=400)

user_bet = screen.textinput(
    title="make your bet", prompt="Which turtle will win the race? Enter a colour: ")


y_positions = [-70, -40, -10, 20, 50, 80]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtles = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:


    for turtle in all_turtles:


        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You've won!")
                is_race_on = False
                break
            else:
                print(f"the winning color is: {winning_color}")
                print("You've lost please try again!")
                is_race_on = False
                break


        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()

