from turtle import Turtle
from ball_page import Ball

class Points(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.leftpoints = 0
        self.rightpoints = 0
        self.displayScoreboard()
    
    def displayScoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.leftpoints, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.rightpoints, align="center", font=("Courier", 80, "normal"))
    
    def calculatePoints(self, val):
        if val == "right":
            self.leftpoints += 1
        else:
            self.rightpoints += 1

        

        

