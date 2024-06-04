from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 500, height = 400)
# setting screen size with width and height in pixels as arguement

colors = ["blue", "green", "yellow", "red", "purple", "orange"]


all_turtles = []
y_positions = [-125, -75, -25, 25, 75, 125]

for turtle_index in range(0, 6):
     new_turtle = Turtle(shape ="turtle")
     new_turtle.penup()
     new_turtle.color(colors[turtle_index])
     new_turtle.goto(x = -230, y = y_positions[turtle_index])
     all_turtles.append(new_turtle)

user_bet = screen.textinput(title = "Give a color", prompt = "Which turtle do you think will win?")
# screen method "textinput" shows a popup screen that shows an input given and users input is kept in user_bet

race_is_on = True
while race_is_on:
     for turtle in all_turtles:
         if turtle.xcor() > 230:
             winning_turtle = turtle.pencolor()     # returns body color of turtle
             race_is_on = False
             if user_bet == winning_turtle:
                 print(f"You have won. {winning_turtle} turtle is the winner.")
             else:
                 print(f"You have lost. {winning_turtle} turtle is the winner.")
         turtle.forward(random.randint(0, 10))




screen.exitonclick()


