import turtle as turtle_module
import random 


turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [(210, 67, 183), (128, 70, 207), (157, 81, 38), (122, 150, 67), (59, 82, 149), (127, 206, 165),
(178, 190, 214), (63, 21, 69), (166, 62, 154), (76, 135, 94), (211, 167, 126), (20, 54, 180)]
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)


    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
tim.dot(20, random.choice(color_list))


screen = turtle_module.Screen()
screen.exitonclick()

