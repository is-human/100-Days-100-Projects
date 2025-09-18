from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
from border import Border
from variables import screen_width, screen_height, screen_width, arena_height
import time

screen = Screen()
screen.setup(screen_width, screen_height)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
perimeter = Border()


screen.listen()
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.08)

    snake.move()

    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score += 1
        if scoreboard.score > scoreboard.highscore:
            scoreboard.highscore = scoreboard.score
            with open(r"highscore.txt", mode="w") as file:
                file.write(f"{scoreboard.highscore}")
        scoreboard.refresh()
    else:
        snake.capture_position()
    
    if -(screen_width/2) <= snake.snake_head.xcor() <= (screen_width/2) and -(arena_height/2) <= snake.snake_head.ycor() <= (arena_height/2):
        pass
    else:
        # game_is_on = False
        for i in snake.whole_snake:
            i.hideturtle()
        snake.whole_snake.clear()
        snake.create_snake()
        scoreboard.score = 0
        scoreboard.refresh()
    
    
    # for instance in snake.whole_snake[1:]:
    #     if snake.snake_head.distance(instance) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()
    #         screen.update()
    #         break
    for instance in snake.whole_snake[1:]:
        if snake.snake_head.distance(instance) < 10:
            for i in snake.whole_snake:
                i.hideturtle()
            snake.whole_snake.clear()
            snake.create_snake()
            scoreboard.score = 0
            scoreboard.refresh()
            screen.update()

screen.exitonclick()