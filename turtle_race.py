from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)

colors = ["red", "orange", "yellow", "blue", "purple", "green", "black"]
name = []

x = -230
y = -160
n = 0

for i in range(7):
    i = Turtle(shape="turtle")
    i.color(colors[n])
    i.penup()
    y += 40
    i.goto(-230, y)
    n += 1
    name.append(i)

is_race_on = True

user_bet = screen.textinput("Make your Bet", "Which turtle win the ")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in name:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"won,! the winning color is {winning_color}")
            else:
                print(f"u lost! the winning color is {winning_color}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()
