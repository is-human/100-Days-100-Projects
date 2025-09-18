from turtle import Turtle
from variables import arena_height, screen_width, player_1_x_value, player_2_x_value, ceiling, floor, right_wall, left_wall, left_shot, right_shot, starting_shot
from scoreboard import Scoreboard
import random

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.setheading(random.choice(starting_shot))
        self.penup()
    def deflect(self, list_1, list_2):
        if self.distance(self.xcor(), ceiling) < 10 or self.distance(self.xcor(), floor) < 10:
            current_heading = self.heading()
            self.setheading(360-current_heading)
        for instance in list_1+list_2:
            if self.distance(player_1_x_value, instance.ycor()) < 15:
                current_heading = self.heading()
                self.setheading(360-(current_heading+180))
                return 1
            elif self.distance(player_2_x_value, instance.ycor()) < 15:
                current_heading = self.heading()
                self.setheading(360-(current_heading+180))
                return -1
    def boundary_check(self):
        if self.distance(right_wall, self.ycor()) < 10:
            self.setheading(random.choice(left_shot))
            self.goto(0,0)
            return 1
        elif self.distance(left_wall, self.ycor()) < 10:
            self.setheading(random.choice(right_shot))
            self.goto(0,0)
            return -1
        else:
            return False