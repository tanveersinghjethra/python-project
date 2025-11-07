from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Guess the Winner", prompt="Guess which color turtle will win the race? (red/blue/green/yellow/purple)")
#the above line gets the user input for their guess
colors = ["blue", "green", "red", "yellow", "purple"]
positions = [-100, -50, 0, 50, 100]
turtles = [] # this will also to add turtle objects to the list later
for i in range(5):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=-250, y=positions[i])
    t.speed("slowest")
    turtles.append(t)

race_on = True

while race_on:
    for turtle in turtles:
        distance = random.randint(1, 10)
        turtle.forward(distance)#this will move the turtle forward by a random distance
        if turtle.xcor() >= 230:#if this x cordinate is greater than or equal to 230, then the turtle has reached the finish line
            race_on = False
            winner = turtle.pencolor()# get the color of the turtle that won
            if user_input.lower() == winner:
                print(f"You won! The {winner} turtle is the winner!")
            else:
                print(f"You lost. The {winner} turtle won the race.")
            break

screen.exitonclick()


# def move_backward():
#     tim.backward(10)
# def turn_left():
#     tim.left(10)
# def turn_right():
#     tim.right(10)
# def clear_screen():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
# screen.listen()#this is used to listen for key presses
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="c", fun=clear_screen)  # Clear the turtle's drawings    

