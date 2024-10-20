import turtle, pandas

my_screen = turtle.Screen()
my_screen.title("US States Game")
image = "blank_states_img.gif"
my_screen.addshape(image)
turtle.shape(image)

# def print_coor(x, y):
#     print(x, y)
# my_screen.onclick(print_coor)


# -------------------------------------------------------------------------------------------------------------------
# SOLUTION 1
states_data = pandas.read_csv("50_states.csv")
states_data_dict = states_data.to_dict()
score = 0
WINNING_SCORE = 50
done = []
while score <= WINNING_SCORE:
    if score != WINNING_SCORE:
        answer = my_screen.textinput(title=f"{score}/50 correct", prompt="Name another state:")
        if answer is None:
            break
        for i in range(50):
            if (states_data_dict["state"][i]).lower() == answer.lower() and states_data_dict["state"][i] not in done:
                done.append(states_data_dict["state"][i])
                score += 1
                temp_object = turtle.Turtle()
                temp_object.penup()
                temp_object.hideturtle()
                state_coors = (states_data_dict["x"][i], states_data_dict["y"][i])
                temp_object.goto(state_coors)
                temp_object.write(arg=states_data_dict["state"][i], align="center", font=("Arial", 8, "normal"))
    else:
        writer = turtle.Turtle()
        writer.penup()
        writer.hideturtle()
        writer.write(arg="YOU WIN!", align="center", font=("Arial", 24, "normal"))
        break


# ------------------------------------------------------------------------------------------------------------------
# SOLUTION 2
# state_data = pandas.read_csv("50_states.csv")
# score = 0
# WINNING_SCORE = 1
# while score <= WINNING_SCORE:
#     if score != WINNING_SCORE:
#         answer = (my_screen.textinput(title=f"Score: {score}/50", prompt="Next Guess?")).title()
#         current_state_df = state_data[state_data.state == answer]
#         if len(current_state_df) != 0:
#             score += 1
#             x_cor = current_state_df["x"]
#             x_cor = (x_cor.to_list())[0]
#             y_cor = current_state_df["y"]
#             y_cor = (y_cor.to_list())[0]
#             coor = (x_cor, y_cor)
#             state = turtle.Turtle()
#             state.penup()
#             state.hideturtle()
#             state.goto(coor)
#             state.write(arg=answer, align="center", font=("Arial", 8, "normal"))
#     elif score == WINNING_SCORE:
#         writer = turtle.Turtle()
#         writer.penup()
#         writer.hideturtle()
#         writer.write(arg="YOU WIN!", align="center", font=("Arial", 24, "normal"))
#         break


my_screen.exitonclick()  # my_screen.mainloop() ##alternative to my_screen.exitonclick()
