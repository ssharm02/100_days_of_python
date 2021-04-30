from turtle import Turtle, Screen
import random
is_race_on = False
tim = Turtle()
screen = Screen()
screen.setup(width=600, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will with the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


def create_turtle():
    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-258, y=y_positions[turtle_index])
        all_turtles.append(new_turtle)


def main_game_logic():
    create_turtle()
    global is_race_on
    global turtle
    if user_bet:
        is_race_on = True
    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You have won The {winning_color} turtle is the winner!")
                else:
                    print(f"You lost, The {winning_color} turtle won the game!")
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)


main_game_logic()
screen.exitonclick()

