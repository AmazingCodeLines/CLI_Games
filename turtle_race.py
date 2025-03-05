"""
Description:
This Python project simulates a colorful Turtle Race using the turtle module. Players place a bet on which turtle will win before the race begins. Once the race starts, each turtle moves forward by a random distance, creating an exciting and unpredictable competition. The game announces the winner at the end and displays whether the player's bet was correct.

Key Features:
✔ Interactive betting system where players choose a turtle color before the race
✔ Six turtles, each with a unique color, racing across the screen
✔ Randomized movement to ensure unpredictable race outcomes
✔ Visual winner announcement using a separate turtle for messages
✔ Closes the screen on user click after displaying results
"""
from turtle import Turtle, Screen
import random

# Set up the screen
race_on = False
screen = Screen()
screen.setup(width=600, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
rainbow_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Rules
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(rainbow_colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[turtle_index])
    all_turtles.append(new_turtle)

# Start race if user placed a bet
if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

        # Check if the turtle crosses the finish line
        if turtle.xcor() > 260:
            race_on = False
            winning_color = turtle.color()[0]

            #Create separate turtle to display the result
            message_turtle = Turtle()
            message_turtle.hideturtle()
            message_turtle.penup()
            message_turtle.goto(0, 0) #Center

            if winning_color == user_bet:
                message_turtle.write("You Win!", align="center", font=("Arial", 120, "bold"))
                print(f"You win! The {winning_color} is the winner!")
            else:
                message_turtle.write(f"You lose! The {winning_color} turtle is the winner!")
                print(f"You lose! The {winning_color} is the winner!")

screen.exitonclick()