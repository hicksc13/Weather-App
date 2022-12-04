from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.color("blue1")
tim.pensize(3)



def move_forwards():
    tim.forward(50)


def move_backwards():
    tim.backward(50)


def move_counter_clock():
    tim.left(90)


def move_clockwise():
    tim.right(90)


def clear_drawing():
    tim.clear()
    tim.reset()
    tim.color("blue1")
    tim.pensize(3)


screen.listen()


screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clock)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_drawing)


screen.exitonclick()

