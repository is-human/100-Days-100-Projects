from turtle import Turtle
import variables

class Border(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = False):
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.upper_lower_borders()
        self.car_lanes()
    def upper_lower_borders(self):
        self.teleport((variables.arena_width/2), -(variables.arena_height/2))
        self.goto(-(variables.arena_width/2), -(variables.arena_height/2))
        self.teleport((variables.arena_width/2), (variables.arena_height/2))
        self.goto(-(variables.arena_width/2), (variables.arena_height/2))
    def car_lanes(self):
        self.lane_distance = variables.lane_spacing
        self.teleport((variables.arena_width/2), -(variables.arena_height/2)+self.lane_distance)
        for i in range(0, variables.arena_height, variables.lane_spacing):
            self.setheading(180)
            for i in range(0, variables.arena_width, variables.dash_spacing*2):
                self.pendown()
                self.forward(variables.dash_spacing)
                self.penup()
                self.forward(variables.dash_spacing)
            self.teleport((variables.arena_width/2), (-(variables.arena_height/2))+self.lane_distance)
            self.lane_distance += variables.lane_spacing