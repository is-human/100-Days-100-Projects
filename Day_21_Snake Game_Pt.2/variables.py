# Main
screen_width = 900
screen_height = 900
arena_width = screen_width-100
arena_height = screen_height-100

# Snake
TOTAL_STARTING_INSTANCES = 3
DEFAULT_SIZE = 20
SNAKE_WIDTH_RATIO = 1
SNAKE_HEIGHT_RATIO = 1
INITIAL_HEADING = 180
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

# Scoreboard
ALIGNMENT = "center"
FONT = "Arial"
SCORE_FONT_SIZE = 15
END_FONT_SIZE = 15
END_FONT_TYPE = "normal"
SCORE_FONT_TYPE = "normal"
END_TEXT = "GAME OVER"

with open(r"highscore.txt", mode="r") as file:
    highscore = file.read()

# Food
# Border