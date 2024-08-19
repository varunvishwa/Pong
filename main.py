from turtle import Screen, Turtle
from paddle_page import RightPaddle, LeftPaddle
from ball_page import Ball
from points_page import Points
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

screen.tracer(0)

rightPaddle = RightPaddle(350,0)
leftPaddle = LeftPaddle(-350,0)
ball = Ball()
points = Points()

screen.listen()
screen.onkey(rightPaddle.go_up, "Up")
screen.onkey(rightPaddle.go_down, "Down")
screen.onkey(leftPaddle.go_up, "w")
screen.onkey(leftPaddle.go_down, "s")

game_on = True

while game_on is True:

    screen.update()
    ball.move_ball()


    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_roof_floor()
    else:
        pass

    if ball.xcor() > 390:
        points.calculatePoints("right")
        points.displayScoreboard()
        ball.reset_ball()
        screen.update()
        time.sleep(1)
        print("Right:", points.rightpoints, "Left:", points.leftpoints)
    elif ball.xcor() < -390:
        points.calculatePoints("left")
        points.displayScoreboard()
        ball.reset_ball()
        screen.update()
        time.sleep(1)
        print("Right:", points.rightpoints, "Left:", points.leftpoints)
    else:
        pass
    

    if ball.distance(rightPaddle) < 50 and ball.xcor() > 335:
        ball.bounce_paddle()
    elif ball.distance(leftPaddle) < 50 and ball.xcor() < -335:
        ball.bounce_paddle()
    else:
        pass


screen.exitonclick()


