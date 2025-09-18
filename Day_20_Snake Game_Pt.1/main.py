from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen_width = 600
screen_height = 600
screen.setup(screen_width, screen_height)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()