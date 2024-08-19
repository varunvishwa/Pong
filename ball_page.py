from turtle import Turtle
from paddle_page import LeftPaddle,RightPaddle
import time

# the ball movement will change only any one of its axis to the opposite side when it collides with any object at anytime

class Ball(Turtle):
    def __init__(self):
        super().__init__()         # here when you call this constructor in the main module, an object of Turtle class is created. Instead of this you can directly import Turtle module in main program and create the object there but it is not good practice.
        self.color("white")        # or else you can inherit Turtle class into Ball class and create normally
        self.shape("circle")
        self.penup()
        self.x_move_value = 0.1
        self.y_move_value = 0.1
        self.rightPoint = 0
        self.leftPoint = 0

    

    def move_ball(self):
        new_x = self.xcor() + self.x_move_value
        new_y = self.ycor() + self.y_move_value
        self.goto(new_x,new_y)
    
    def bounce_roof_floor(self):
            self.y_move_value *= -1
            new_x = self.xcor()
            new_y = self.ycor() + self.y_move_value
            self.goto(new_x,new_y)
    
    def bounce_paddle(self):
            self.x_move_value *= -1
            new_x = self.xcor() + self.x_move_value
            new_y = self.ycor()
            self.goto(new_x,new_y)
    
    def reset_ball(self):
         self.goto(0,0)
         time.sleep(1)
    

    