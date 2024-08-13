import turtle
import random

color_list = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20),
              (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55),
              (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222),
              (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22),
              (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203),
              (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)]

tim = turtle.Turtle()

turtle.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

def moving_forward():
    tim.penup()
    tim.forward(50)
    tim.pendown()

def starting_new_line():
    tim.penup()
    tim.right(180)
    tim.forward(450)
    tim.right(90)
    tim.forward(50)
    tim.right(90)



for line in range(1, 10 + 1):
    for _ in range(1, 10 + 1):
        tim.dot(20, random.choice(color_list))
        if _ != 10:
            moving_forward()
    starting_new_line()




screen = turtle.Screen()
screen.exitonclick()

# import turtle as turtle_module
# import random
#
# turtle_module.colormode(255)
# tim = turtle_module.Turtle()
# tim.speed("fastest")
# tim.penup()
# tim.hideturtle()
# color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100
#
# for dot_count in range(1, number_of_dots + 1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)
#
#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)
#
#
#
#
#
#
#
#
#
# screen = turtle_module.Screen()
# screen.exitonclick()
#
#
