from turtle import Turtle
from variables import screen_width, arena_height

class Border(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.teleport(-(screen_width/2), -(arena_height/2))
        self.goto((screen_width/2), -(arena_height/2))
        self.goto((screen_width/2), (arena_height/2))
        self.goto(-(screen_width/2), (arena_height/2))
        self.goto(-(screen_width/2), -(arena_height/2))