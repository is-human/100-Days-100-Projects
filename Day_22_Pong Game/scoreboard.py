from turtle import Turtle
from variables import arena_height, ceiling

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-50, ceiling-50)
        self.write(0, font=["Arial", 20, "bold"], align="left")
        self.goto(50, ceiling-50)
        self.write(0, font=["Arial", 20, "bold"], align="right")
    def score_update(self, updated_score, static_score, player):
        if player == 1:
            self.clear()
            self.goto(-50, ceiling-50)
            self.write(updated_score,font=["Arial", 20, "bold"], align="left")
            self.goto(50, ceiling-50)
            self.write(static_score,font=["Arial", 20, "bold"], align="right")
        elif player == -1:
            self.clear()
            self.goto(-50, ceiling-50)
            self.write(static_score,font=["Arial", 20, "bold"], align="left")
            self.goto(50, ceiling-50)
            self.write(updated_score,font=["Arial", 20, "bold"], align="right")
        pass