from turtle import Turtle

class RightPaddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x,y)

    def go_up(self): 
        new_y = self.ycor() + 20
        new_x = self.xcor()
        self.goto(new_x,new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        new_x = self.xcor() 
        self.goto(new_x,new_y)

class LeftPaddle(RightPaddle):
        def __init__(self,x,y) -> None:  #all input attributes being used in the child class
              super().__init__(x,y)      #all input attribute attributes being inherited into the child class
              self.goto(x,y)



