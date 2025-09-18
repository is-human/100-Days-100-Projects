from turtle import Turtle
import variables

class Player(Turtle):
    def __init__(self, shape = "turtle", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.shapesize(stretch_wid=(20/variables.lane_spacing), stretch_len=(20/variables.lane_spacing))
        self.color("white")
        self.penup()
        self.setheading(90)
        self.teleport(0, -(variables.arena_height/2)-(variables.lane_spacing/2))
    def move_forward(self):
        self.setheading(90)
        self.forward(variables.lane_spacing)
    def move_back(self):
        self.setheading(-90)
        self.forward(variables.lane_spacing)
    def move_left(self):
        self.setheading(180)
        self.forward(variables.lane_spacing)
    def move_right(self):
        self.setheading(0)
        self.forward(variables.lane_spacing)
    def level_check(self, scoreboard):
        if self.ycor() > (variables.arena_height/2):
            scoreboard.update_score()
            self.teleport(0, -(variables.arena_height/2)-(variables.lane_spacing/2))
    def crash_detection(self):
        for i in variables.car_manager:
            if self.ycor() == i.ycor() and self.distance(i.xcor(), i.ycor()) < (20/variables.lane_spacing)*20:
                return False
        return True