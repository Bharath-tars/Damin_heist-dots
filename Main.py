import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(114, 98, 59), (37, 20, 33), (18, 12, 33), (63, 39, 26), (148, 141, 82), (178, 164, 100), (82, 103, 75), (94, 76, 86), (80, 70, 35), (239, 204, 113), (92, 52, 42), (77, 55, 64), (83, 78, 96), (41, 54, 37), (254, 230, 142), (62, 57, 77), (54, 73, 49), (117, 139, 104), (131, 150, 123), (157, 139, 148), (159, 115, 103), (141, 119, 127), (146, 141, 158), (126, 121, 141), (226, 211, 219), (213, 210, 223), (203, 183, 190), (219, 180, 170), (190, 185, 204), (180, 200, 168)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen = turtle_module.Screen()
screen.exitonclick()
