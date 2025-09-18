import random

# Main
screen_width = 800
screen_height = 500
arena_width = screen_width-100
arena_height = screen_height-100

# Borders
b_pensize = 1
left_wall = -(arena_width/2)
right_wall = (arena_width/2)

# Scoreboard
ceiling = (arena_height/2)
floor = -(arena_height/2)

# Players
player_1_length = 5
player_2_length = 5
player_1_x_value = -(arena_width/2)+50
player_2_x_value = (arena_width/2)-50
move_rate = 40

# Ball
running_score_1 = 0
running_score_2 = 0
right_shot = [random.randint(10, 80), random.randint(-80, -10)]
left_shot = [random.randint(100, 170), random.randint(-170, -100)]
starting_shot = right_shot + left_shot