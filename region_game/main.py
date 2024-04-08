import turtle
import pandas
# from PIL import Image


screen = turtle.Screen()
turtle.title("Morocco Region Game")

image = "morocco_map.gif"

screen.addshape(image)
turtle.shape(image)


# Function to get mouse click coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv("morocco_states.csv")
guessed_states = []
score = 0

while len(guessed_states) < 13:

    user_answer = screen.textinput(title=f"{score}/12 Guess The Region", prompt="Write a region you know").title()
    print(user_answer)

    regions = data["region"].to_list()
    print(regions)

    if user_answer == "Exit":
        break

    if not user_answer in regions:
        continue
    else:
        if user_answer in guessed_states:
            print("already guessed it")
            continue
        else:
            score+=1
            guessed_states.append(user_answer)
            word = turtle.Turtle()
            word.hideturtle()
            word.penup()
            answer_row = data[data.region == user_answer]
            word.goto(int(answer_row.x), int(answer_row.y))
            word.write(answer_row.region.item())


