import turtle
import random

color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), 
 (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), 
 (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

turtle.colormode(255)
tommy = turtle.Turtle()
tommy.hideturtle()
tommy.penup()
tommy.setpos(-350,-300)
tommy.speed("fastest")

goal_rows = 12
goal_columns = 15
spacing = 50
row_completed = 0

while row_completed < goal_rows:
    for column in range(goal_columns):
        random_color = random.choice(color_list)
        tommy.dot(20, random_color)
        tommy.forward(spacing)

    row_completed += 1

    if row_completed < goal_rows:
        tommy.left(90)
        tommy.forward(60)
        tommy.left(90)
        tommy.forward(spacing*goal_columns)
        tommy.left(180)

screen = turtle.Screen()
screen.exitonclick()