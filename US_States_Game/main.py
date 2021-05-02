import turtle
import pandas

screen = turtle.Screen()
screen.title(f"US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

score = 0


def get_mouse_click_coor(x, y):
    print(x, y)


def read_states_csv():
    states_data = pandas.read_csv("50_states.csv")
    return states_data


def count_missing_states():
    # replaced with list comprehension
    local_missing_states = [state
                            for state in panda_states if state not in guessed_states]
    # for state in panda_states:
    #     if state not in guessed_states:
    #         local_missing_states.append(state)
    return local_missing_states


# game logic
data = read_states_csv()
panda_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f" {len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name? ").title()

    if answer_state == "Exit":
        missing_states = count_missing_states()
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break
    if answer_state in panda_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        score += 1
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
