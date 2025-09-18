from turtle import Turtle
from variables import screen_width, arena_height
import random

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        random_x = random.randint(-round(((screen_width/2)-20)), round(((screen_width/2)-20)))
        random_y = random.randint(-round(((arena_height/2)-20)), round(((arena_height/2)-20)))
        self.teleport(random_x, random_y)