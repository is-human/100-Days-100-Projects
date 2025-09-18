import random
# Screen
# Ensure the screen height is divisble by lane spacing
# ensure the screen width is divisble by dash spacing.
screen_width = 500
screen_height = 600
arena_width = screen_width
arena_height = screen_height-100

lane_spacing = 25
dash_spacing = 10

car_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
car_manager = []
maximum_lanes = (arena_height/lane_spacing)
number_of_spawned_cars = random.randrange(0, int(maximum_lanes*0.5))

speed_increase = 0.75