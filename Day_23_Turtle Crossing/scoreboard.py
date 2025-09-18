from turtle import Turtle
import variables

class Scoreboard(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = False):
        super().__init__(shape, undobuffersize, visible)
        self.level = 0
        self.color("white")
        self.penup()
        self.teleport(-(variables.arena_width/2)+25, (variables.arena_height/2)+15)
        self.write(f"Level: {self.level}", font=("Courier", 12, "bold"))
    def update_score(self):
        self.clear()
        self.level += 1
        self.teleport(-(variables.arena_width/2)+25, (variables.arena_height/2)+15)
        self.write(f"Level: {self.level}", font=("Courier", 12, "bold"))
    def game_over(self):
        self.teleport(-52,0)
        self.write("GAME OVER\n" + f"Score: {self.level}", font=("Courier", 15, "bold"))