from turtle import Turtle
import math

TOTAL_STARTING_INSTANCES = 3
DEFAULT_SIZE = 20
SNAKE_WIDTH_RATIO = 1
SNAKE_HEIGHT_RATIO = 1
INITIAL_HEADING = 0
PACE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
SNAKE_HEAD_COLOR = "white"
SNAKE_BODY_COLOR = "white"
SNAKE_HEAD_PENCOLOR = "red"
SNAKE_BODY_PENCOLOR = "green"
SNAKE_HEAD_SHAPE = "square"
SNAKE_BODY_SHAPE = "square"

class Snake:
    def __init__(self) -> None:
        self.whole_snake = []
        self.create_snake()

    def create_snake(self):
        self.snake_head = Turtle(SNAKE_HEAD_SHAPE)
        self.whole_snake.append(self.snake_head)
        self.snake_head.color(SNAKE_HEAD_COLOR)
        self.snake_head.pencolor(SNAKE_HEAD_PENCOLOR)
        self.snake_head.penup()
        self.snake_head.resizemode("user")
        self.snake_head.shapesize(SNAKE_WIDTH_RATIO, SNAKE_HEIGHT_RATIO)
        self.snake_head.setheading(INITIAL_HEADING)

        for instances in range(TOTAL_STARTING_INSTANCES-1):
            self.snake_body = Turtle(SNAKE_BODY_SHAPE)
            self.snake_body.color(SNAKE_BODY_COLOR)
            self.snake_body.pencolor(SNAKE_BODY_PENCOLOR)
            self.snake_body.penup()
            self.snake_body.resizemode("user")
            self.snake_body.shapesize(SNAKE_WIDTH_RATIO, SNAKE_HEIGHT_RATIO)
            self.xy_coordinates = self.whole_snake[-1].position()
            self.current_heading = self.whole_snake[-1].heading()
            self.x2 = self.xy_coordinates[0] - (DEFAULT_SIZE*SNAKE_HEIGHT_RATIO) * math.cos(math.radians(self.current_heading))
            self.y2 = self.xy_coordinates[1] - (DEFAULT_SIZE*SNAKE_HEIGHT_RATIO) * math.sin(math.radians(self.current_heading))
            self.snake_body.setheading(self.current_heading)
            self.snake_body.teleport(self.x2, self.y2)
            self.whole_snake.append(self.snake_body)
    
    def move(self):
        for instance in reversed(self.whole_snake[1:]):
            instance_index = self.whole_snake.index(instance)
            new_coordinates = self.whole_snake[instance_index-1].position()
            new_heading = self.whole_snake[instance_index-1].heading()
            instance.teleport(new_coordinates[0], new_coordinates[1])
            instance.setheading(new_heading)
        self.whole_snake[0].forward(PACE)
    def move_left(self):
        if self.whole_snake[0].heading() != RIGHT:
            self.whole_snake[0].setheading(LEFT)
    def move_right(self):
        if self.whole_snake[0].heading() != LEFT:
            self.whole_snake[0].setheading(RIGHT)
    def move_up(self):
        if self.whole_snake[0].heading() != DOWN:
            self.whole_snake[0].setheading(UP)
    def move_down(self):
        if self.whole_snake[0].heading() != UP:
            self.whole_snake[0].setheading(DOWN)