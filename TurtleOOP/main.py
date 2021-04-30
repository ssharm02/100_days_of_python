from turtle import Turtle, Screen
import heroes
import random
# alias name
import turtle as t

tim = Turtle()
tim.shape("triangle")
# tim.color("black")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
t.colormode(255)


def move_turtle():
    for i in range(4):
        tim.forward(100)
        tim.right(90)


def generate_hero_name():
    print(heroes.gen())


def generate_dash_lines():
    for i in range(15):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()


def draw_diff_shapes(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_tuple = (r, b, g)
    return rgb_tuple


def random_walk():
    tim.pensize(15)
    for i in range(0, 200):
        print("Random color is random_color ", random_color())
        tim.color(random_color())
        tim.speed(i)
        tim.forward(30)
        tim.setheading(random.choice(directions))


def draw_spirograph(size_of_gap):
    tim.speed("fastest")

    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)
# random_walk()
# for shape_side in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_diff_shapes(shape_side)


# draw_diff_shapes(12)
# generate_dash_lines()
generate_hero_name()
# move_turtle()
screen = Screen()
screen.exitonclick()
