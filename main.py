from turtle import Turtle, Screen
import random


screen = Screen()

is_race_on = False
# Set screen size
screen.setup(width=500, height=400)
# Pop up screen for input and prompt for user to bet on specific turtle
user_choice = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
# Colors for each turtle
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# Positions for each turtle to make them line up
y_positions = [-70, -40, -10, 20, 50, 80]
# Store all turtle object
all_turtles = []


def start_lineup():
    """ Initialise turtles, give them different colours and line them up for the start of the race """
    for turtle_index in range(0, 6):
        # Init turtle and give turtle shape
        new_turtle = Turtle(shape="turtle")
        # Move pen up to avoid line
        new_turtle.penup()
        # Give turtle unique color
        new_turtle.color(colors[turtle_index])
        # Move turtle to very left edge
        new_turtle.goto(x=-240, y=y_positions[turtle_index])
        # Append turtles to list
        all_turtles.append(new_turtle)


if user_choice:
    is_race_on = True
    start_lineup()

while is_race_on:

    for turtle in all_turtles:
        # Turtle has won if he gets to 230 x cor
        # 230 is cor where turtle head touch right most of screen
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            # Check if user won
            if winning_color == user_choice:
                screen.title(f"You've won! The {winning_color} turtle is the winner")
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                screen.title(f"You've lost! The {winning_color} turtle is the winner")
                print(f"You lost! The {winning_color} turtle is the winner")
            is_race_on = False
        # Loop through turtles and move them by a random int
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
