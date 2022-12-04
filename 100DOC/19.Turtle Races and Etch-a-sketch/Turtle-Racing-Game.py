from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your Bet!", prompt = "Which turtle will win? Enter color: ")
colors = ["red", "blue", "green", "orange", "purple", "yellow", "dark green", "magenta"]
y_positions = [-100, -70, -40, -10, 20, 50, 80, 110]
all_turtles = []




for turtle_index in range(0,8):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x= -230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:


    for turtle in all_turtles:


        if turtle.xcor() > 230:


            is_race_on = False
            winning_color = turtle.pencolor()


            if winning_color == user_bet:

                print(f"You Won!! The Winning color was {winning_color}")
            else:
                print(f"You Lost!! The Winning color was {winning_color}")


        rand_dist = random.randint(2,15)
        turtle.forward(rand_dist)









# tom = Turtle(shape="turtle")
# tom.penup()
# tom.color("yellow")
# tom.goto(x= -230, y= -50)

# ted = Turtle(shape="turtle")
# ted.color("green")
# ted.penup()
# ted.goto(x= -230, y= 0)

# terry = Turtle(shape="turtle")
# terry.color("blue")
# terry.penup()
# terry.goto(x= -230, y= 50)

# tod = Turtle(shape="turtle")
# tod.color("orange")
# tod.penup()
# tod.goto(x= -230, y= 100)


screen.exitonclick()