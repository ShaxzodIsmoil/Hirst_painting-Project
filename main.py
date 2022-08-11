"""
Auther by Shaxzodbek Rafiqov
"""

import turtle as t
import random


t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_paint = [(237, 231, 214), (218, 234, 224), (141, 176, 206), (25, 32, 48), (28, 105, 156), (208, 161, 112), (238, 222, 234), (230, 211, 94), (131, 31, 64), (5, 162, 195), (182, 45, 84)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_paint))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)









screen = t.Screen()
screen.exitonclick()