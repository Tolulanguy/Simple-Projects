import turtle
screen = turtle.Screen()
screen.title("U.S. State Game")

image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

user_input = screen.textinput(title="Guess the name", prompt="Enter the name of the state")

def get_mouse_click_coor(x, y):
    print(x, y)
turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()


