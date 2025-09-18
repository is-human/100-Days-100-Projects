from turtle import Turtle
import variables
import math

class Snake:
    def __init__(self) -> None:
        self.whole_snake = []
        self.create_snake()

    def create_snake(self):
        self.snake_head = Turtle(variables.SNAKE_HEAD_SHAPE)
        self.whole_snake.append(self.snake_head)
        self.snake_head.color(variables.SNAKE_HEAD_COLOR)
        self.snake_head.pencolor(variables.SNAKE_HEAD_PENCOLOR)
        self.snake_head.penup()
        self.snake_head.resizemode("user")
        self.snake_head.shapesize(variables.SNAKE_WIDTH_RATIO, variables.SNAKE_HEIGHT_RATIO)
        self.snake_head.setheading(variables.INITIAL_HEADING)

        for instances in range(variables.TOTAL_STARTING_INSTANCES-1):
            self.snake_body = Turtle(variables.SNAKE_BODY_SHAPE)
            self.snake_body.color(variables.SNAKE_BODY_COLOR)
            self.snake_body.pencolor(variables.SNAKE_BODY_PENCOLOR)
            self.snake_body.penup()
            self.snake_body.resizemode("user")
            self.snake_body.shapesize(variables.SNAKE_WIDTH_RATIO, variables.SNAKE_HEIGHT_RATIO)
            self.xy_coordinates = self.whole_snake[-1].position()
            self.current_heading = self.whole_snake[-1].heading()
            self.x2 = self.xy_coordinates[0] - (variables.DEFAULT_SIZE*variables.SNAKE_HEIGHT_RATIO) * math.cos(math.radians(self.current_heading))
            self.y2 = self.xy_coordinates[1] - (variables.DEFAULT_SIZE*variables.SNAKE_HEIGHT_RATIO) * math.sin(math.radians(self.current_heading))
            self.snake_body.setheading(self.current_heading)
            self.snake_body.teleport(self.x2, self.y2)
            self.whole_snake.append(self.snake_body)
    
    def capture_position(self):
        self.capture_coordinates = self.whole_snake[-1].position()
        self.capture_heading = self.whole_snake[-1].heading()
    
    def extend(self):
        self.snake_body = Turtle(variables.SNAKE_BODY_SHAPE)
        self.snake_body.color(variables.SNAKE_BODY_COLOR)
        self.snake_body.pencolor(variables.SNAKE_BODY_PENCOLOR)
        self.snake_body.penup()
        self.snake_body.resizemode("user")
        self.snake_body.shapesize(variables.SNAKE_WIDTH_RATIO, variables.SNAKE_HEIGHT_RATIO)
        self.snake_body.setheading(self.capture_heading)
        self.snake_body.teleport(self.capture_coordinates[0], self.capture_coordinates[1])
        self.whole_snake.append(self.snake_body)

    def move(self):
        for instance in reversed(self.whole_snake[1:]):
            instance_index = self.whole_snake.index(instance)
            new_coordinates = self.whole_snake[instance_index-1].position()
            new_heading = self.whole_snake[instance_index-1].heading()
            instance.teleport(new_coordinates[0], new_coordinates[1])
            instance.setheading(new_heading)
        self.whole_snake[0].forward(variables.PACE)
    def move_left(self):
        if self.whole_snake[0].heading() != variables.RIGHT:
            self.whole_snake[0].setheading(variables.LEFT)
    def move_right(self):
        if self.whole_snake[0].heading() != variables.LEFT:
            self.whole_snake[0].setheading(variables.RIGHT)
    def move_up(self):
        if self.whole_snake[0].heading() != variables.DOWN:
            self.whole_snake[0].setheading(variables.UP)
    def move_down(self):
        if self.whole_snake[0].heading() != variables.UP:
            self.whole_snake[0].setheading(variables.DOWN)