from turtle import Turtle
import variables

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.teleport(0, (variables.arena_height/2)-30)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.highscore = int(variables.highscore)
        self.write(f"Score: {self.score}", False, variables.ALIGNMENT, (variables.FONT, variables.SCORE_FONT_SIZE, variables.SCORE_FONT_TYPE))
        self.teleport(0, (variables.arena_height/2)-50)
        self.write(f"Highscore: {self.highscore}", False, variables.ALIGNMENT, (variables.FONT, variables.END_FONT_SIZE, variables.END_FONT_TYPE))
    def refresh(self):
        self.clear()
        self.teleport(0, (variables.arena_height/2)-30)
        self.write(f"Score: {self.score}", False, variables.ALIGNMENT, (variables.FONT, variables.SCORE_FONT_SIZE, variables.SCORE_FONT_TYPE))
        self.teleport(0, (variables.arena_height/2)-50)
        self.write(f"Highscore: {self.highscore}", False, variables.ALIGNMENT, (variables.FONT, variables.END_FONT_SIZE, variables.END_FONT_TYPE))
    # def game_over(self):
    #     self.teleport(0, 0)
    #     self.write(variables.END_TEXT, False, variables.ALIGNMENT, (variables.FONT, variables.END_FONT_SIZE, variables.END_FONT_TYPE))
    # def round_over(self):
    #     self.teleport(0, (variables.arena_height/2)-50)
    #     self.write(f"Highscore: {self.highscore}", False, variables.ALIGNMENT, (variables.FONT, variables.END_FONT_SIZE, variables.END_FONT_TYPE))