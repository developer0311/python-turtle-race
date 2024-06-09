from turtle import Turtle, Screen
import random



screen = Screen()
screen.setup(width = 1000, height = 800)

colors = ["red", "green", "violet", "blue", "orange", "pink"]
y_positions = [-80, -50, -20, 20, 50, 80]
turtles = []

is_race_on = False
user_turtle = screen.textinput(title = "Make your bet", prompt= f"Which turtle will win the race {colors}\nEnter a color: ")

for i in range (6):
    new_turtle = Turtle("turtle")
    # new_turtle.speed("fastest")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x = -480, y = y_positions[i])
    turtles.append(new_turtle)

if user_turtle:
    is_race_on = True


while is_race_on:
    for turtle in turtles:

        turtle.forward(random.randint(0,10))

        if turtle.xcor() >= 480:
            is_race_on = False

            if user_turtle.lower() == turtle.pencolor():
                print(f"You won🎉\n{turtle.pencolor().title()} turtle won the race.")
            else:
                print(f"You lost😢\n{turtle.pencolor().title()} turtle won the race.")





screen.exitonclick()