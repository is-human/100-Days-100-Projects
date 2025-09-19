import turtle
import pandas

image = r"blank_states_img.gif"
raw_data = pandas.read_csv(r"50_states.csv")

screen = turtle.Screen()
screen.title("U.S.A. Geography Quiz")
screen.addshape(image)
turtle.shape(image)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("black")

number_of_states = raw_data.state.count()

q_state = screen.textinput(title="Guess the State", prompt="Can you name a state?").title()

states_guessed = []
correct_answers = 0

while correct_answers < number_of_states:
    row = 0
    for state in raw_data.state:
        if q_state == state and state not in states_guessed:
            x_coor = raw_data.iloc[row, 1]
            y_coor = raw_data.iloc[row, 2]
            pen.goto(x_coor, y_coor)
            pen.write(state)
            states_guessed.append(state)
            correct_answers += 1
        row += 1
    if correct_answers < number_of_states:
        q_state = screen.textinput(title=f"{correct_answers}/{number_of_states} States Correct", prompt="What's another state name?").title()
        if q_state == "Exit":
            missed_states = [i for i in raw_data.state if i not in states_guessed]

            # for state in raw_data.state:
            #     if state not in states_guessed:
            #         missed_states.append(state)

            incorrect_answers = len(missed_states)
            print("\nYou still need practice :(\n")
            print(f"You missed: {incorrect_answers}/{number_of_states}")
            print("Take a look!\n")
            print(missed_states)
            new_data = pandas.DataFrame(missed_states)
            new_data.to_csv(r"missed_states.csv")
            break
    else:
        print("Congradulations! You know your states!")
        break

# screen.exitonclick()

# turtle.mainloop()

# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)

# print(raw_data[raw_data.state == "Texas"]["x"])