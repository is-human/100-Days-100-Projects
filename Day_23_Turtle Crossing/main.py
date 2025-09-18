from turtle import Screen
import variables
import player
import border
import cars
import scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.setup(variables.screen_width, variables.screen_height)
screen.tracer(0)

border = border.Border()
scoreboard = scoreboard.Scoreboard()
cars = cars.Cars()
player = player.Player()

game_is_on = True

screen.listen()
screen.onkey(player.move_forward, "Up")
screen.onkey(player.move_back, "Down")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

while game_is_on == True:
    player.level_check(scoreboard)
    cars.move_forward(scoreboard.level)
    cars.count += 1
    if cars.count%20 == 0:
        cars.incoming_cars()
    game_is_on = player.crash_detection()
    screen.update()
    time.sleep(0.01)

scoreboard.game_over()

screen.exitonclick()