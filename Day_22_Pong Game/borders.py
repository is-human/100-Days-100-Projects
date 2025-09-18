from turtle import Turtle
from variables import screen_width, arena_height, b_pensize, left_wall, right_wall, ceiling, floor

class Borders(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.pensize(b_pensize)
        self.outside_border()
        self.divider()
    def outside_border(self):
        self.teleport(left_wall, floor)
        self.goto(right_wall, floor)
        self.goto(right_wall, ceiling)
        self.goto(left_wall, ceiling)
        self.goto(left_wall, floor)
        self.penup()
    def divider(self):
        self.goto(0, floor)        
        self.setheading(90)
        self.shape("square")
        self.shapesize(stretch_wid=0.05, stretch_len=1)
        for i in range(0, arena_height-25, 25):
            self.forward(25)
            self.stamp()