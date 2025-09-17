from turtle import Turtle, Screen
import random

screen = Screen()
screen_height = 400
screen_width = 500
screen.setup(screen_width, screen_height)
color = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
user_bet = screen.textinput("Choose Your Turtle", "Place Your Bet\n" + "Which turtle will win the race?!\n" + "Enter a color (red/orange/yellow/green/blue/purple): ").lower()

order = 0
edge_space = 50
start_x_axis = (-(screen_width/2)+ edge_space)
start_y_axis = (-(screen_height/2)+ edge_space)
game_online = True
winners = []

for instance in color:
    new_turtle = Turtle(shape="turtle")
    turtles.append(new_turtle)
    new_turtle.color(color[order])
    new_turtle.penup()
    new_turtle.setposition(start_x_axis, start_y_axis)
    order += 1
    start_y_axis += (screen_height-edge_space)/len(color)

while game_online:
    for instance in turtles:
        pace = random.randint(0,10)
        instance.forward(pace)
    
    order = 0
    for instance in turtles:
        if instance.xcor() >= (screen_width/2)-30:
            winners.append(color[order])
            game_online = False
        order += 1
    if len(winners) > 1:
        if user_bet in winners:
            print(f"You tied! {winners} all finsihed in first!")
        else:
            print(f"You lost! {winners} all tied in first.")
    elif len(winners) == 1:
        if user_bet in winners:
            print(f"You Won! Your {winners[0].title()} Turtle Finished First!")
        else:
            print(f"Your Turtle Has Fallen! {winners[0].title()} Won The Race.")

screen.exitonclick()