import turtle
import pandas as pd

# Objects
screen = turtle.Screen()
screen.title("US States Game")

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

# Data
raw = pd.read_csv("50_states.csv")
data = raw

# Game setup
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state name?").title()
    state_data = raw[raw.state == answer_state]
    if not state_data.empty:
        if answer_state not in guessed_states:
            writer.setpos(state_data["x"].item(), state_data["y"].item())
            writer.write(state_data["state"].item())
            guessed_states.append(answer_state)
        else:
            print("You've already guessed that.")
    else:
        print("That's not a state.")


turtle.mainloop()
