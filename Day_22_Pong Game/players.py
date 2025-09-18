from turtle import Turtle
from variables import player_1_length, player_2_length, player_1_x_value, player_2_x_value, ceiling, floor, move_rate

class Players(Turtle):
    def __init__(self, shape: str = "square", visible: bool = False) -> None:
        super().__init__(shape, visible)
        self.hideturtle()
        self.player_1 = []
        self.player_2 = []
        self.create_players()
    def create_players(self):
        distance = 0
        for instance in range(player_1_length):
            instance = Turtle(shape="square")
            instance.color("white")
            instance.shapesize(stretch_len=0.5, stretch_wid=0.8)
            instance.penup()
            instance.goto(player_1_x_value, distance)
            self.player_1.append(instance)
            distance -= 15

        distance = 0
        for instance in range(player_2_length):
            instance = Turtle(shape="square")
            instance.color("white")
            instance.shapesize(stretch_len=0.5, stretch_wid=0.8)
            instance.penup()
            instance.goto(player_2_x_value, distance)
            self.player_2.append(instance)
            distance -= 15
        pass
    def player_1_move_up(self):
        # if self.player_1[1].distance(self.player_1[1].xcor(), ceiling) < 10:
        if self.player_1[0].ycor() >= ceiling-20:
            pass
        else:
            for instance in range(len(self.player_1)):
                y_coordinates = self.player_1[instance].ycor()
                self.player_1[instance].goto(player_1_x_value, y_coordinates+move_rate)
    def player_1_move_down(self):
        if self.player_1[-1].ycor() <= floor+20:
            pass
        else:
            for instance in range(len(self.player_1)):
                y_coordinates = self.player_1[instance].ycor()
                self.player_1[instance].goto(player_1_x_value, y_coordinates-move_rate)
    def player_2_move_up(self):
        if self.player_2[0].ycor() >= ceiling-20:
            pass
        else:
            for instance in range(len(self.player_2)):
                y_coordinates = self.player_2[instance].ycor()
                self.player_2[instance].goto(player_2_x_value, y_coordinates+move_rate)
    def player_2_move_down(self):
        if self.player_2[-1].ycor() <= floor+20:
            pass
        else:
            for instance in range(len(self.player_2)):
                y_coordinates = self.player_2[instance].ycor()
                self.player_2[instance].goto(player_2_x_value, y_coordinates-move_rate)