from turtle import Screen
from variables import screen_width, screen_height
from borders import Borders
from scoreboard import Scoreboard
from players import Players
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.title("My Pong Game")
screen.setup(screen_width, screen_height)
screen.tracer(0)

borders = Borders()
scoreboard = Scoreboard()
players = Players()
ball = Ball()

screen.listen()
screen.onkey(players.player_1_move_up, "w")
screen.onkey(players.player_1_move_down, "s")
screen.onkey(players.player_2_move_up, "Up")
screen.onkey(players.player_2_move_down, "Down")

score_1 = 0
score_2 = 0
ballspeed = 2
game_on = True


while game_on == True:
    screen.update()
    time.sleep(.01)
    ball.forward(ballspeed)
    speed = ball.deflect(players.player_1, players.player_2)
    points = ball.boundary_check()
    if speed == 1 or speed == -1:
        ballspeed += 0.20
    elif points == 1 or points == -1:
        ballspeed = 2
    if points == 1:
        score_1 += 1
        scoreboard.score_update(score_1, score_2, points)
    elif points == -1:
        score_2 += 1
        scoreboard.score_update(score_2, score_1, points)
    if score_1 == 10 or score_2 == 10:
        game_on = False
        print("Game Over!")
        if score_1 == 10:
            print("Player One Won!")
        else:
            print("Player Two Won!")

screen.exitonclick()