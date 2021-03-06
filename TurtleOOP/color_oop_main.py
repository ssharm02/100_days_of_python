import colorgram
import random
import turtle as turtle_module
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

full_colors = [(248, 247, 246), (235, 243, 248), (249, 241, 246), (243, 250, 246), (21, 114, 173), (142, 163, 184), (204, 137, 166), (190, 173, 17), (145, 17, 32), (238, 213, 62), (67, 24, 31), (17, 138, 59), (219, 161, 88), (122, 71, 100), (49, 29, 26), (197, 65, 28), (7, 107, 64), (227, 169, 197), (240, 78, 29), (29, 177, 84), (21, 172, 188), (243, 214, 4), (110, 192, 140), (182, 94, 115), (35, 37, 46), (188, 182, 213), (157, 206, 215), (240, 168, 154), (147, 215, 171), (127, 32, 26)]


def draw_turtle():
    tim.setheading(225)
    tim.forward(250)
    tim.setheading(0)
    number_of_dots = 100
    for dot_count in range(1, number_of_dots + 1):
        tim.dot(20, random.choice(full_colors))
        tim.forward(50)

        if dot_count % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)


def extract_colors_from_img():
    colors = colorgram.extract("img.jpg", 30)
    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    print(rgb_colors)


draw_turtle()
screen = turtle_module.Screen()
screen.exitonclick()