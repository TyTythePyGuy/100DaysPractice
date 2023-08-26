###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
# TODO: 10 x 10 row of dots
# TODO: 20 in size and spaced apart 50
import turtle as t
from turtle import Screen
import random

hirsty = t.Turtle()
t.colormode(255)
hirsty.speed("fastest")
hirsty.shape("turtle")

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


def row_of_colors():
    #hirsty.hideturtle()
    for _ in range(10):
        hirsty.begin_fill()
        hirsty.pd()
        hirsty.dot(20, random.choice(color_list))
        hirsty.end_fill()
        hirsty.pu()
        hirsty.forward(50)
        hirsty.pd()
        hirsty.pu()
    hirsty.setheading(180)
    hirsty.forward(500)
    hirsty.setheading(90)
    hirsty.forward(50)
    hirsty.setheading(0)


hirsty.pu()
hirsty.setheading(225)
hirsty.forward(250)
hirsty.setheading(0)
for _ in range(10):
    row_of_colors()


screen = Screen()
screen.exitonclick()
