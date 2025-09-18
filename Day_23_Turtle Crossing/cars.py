from turtle import Turtle
import variables
import random

class Cars(Turtle):
    def __init__(self, shape = "square", undobuffersize = 1000, visible = False):
        super().__init__(shape, undobuffersize, visible)
        self.count = 0
        self.incoming_cars()
    def incoming_cars(self):
        for i in range(random.randrange(1, int(variables.maximum_lanes*0.5))):
            i = Turtle("square")
            i.shapesize(stretch_wid=(20/variables.lane_spacing), stretch_len=(variables.lane_spacing/20))
            i.color(random.choice(variables.car_colors))
            i.penup()
            i.setheading(180)
            i.teleport((variables.arena_width/2), (-(variables.arena_height/2)-(variables.lane_spacing/2))+(random.randint(1, int(variables.maximum_lanes))*variables.lane_spacing))
            variables.car_manager.append(i)
    def move_forward(self, game_level):
        for i in variables.car_manager:
            if i.xcor() > -(variables.arena_width/2)-50:
                i.forward(1+(game_level*variables.speed_increase))