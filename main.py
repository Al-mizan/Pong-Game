from turtle import Screen
from time import sleep

from leftrightcontroller import LeftRightController
from middleborder import MiddleBorder
from ball import Ball

screen = Screen()
screen.setup(width=1000, height=600)
screen.title("Pong Game")
screen.bgcolor('grey20')
screen.colormode(256)
screen.tracer(0)


leftController = LeftRightController('left')
rightController = LeftRightController('right')
middleBorder = MiddleBorder()
ball = Ball()

screen.listen()
screen.onkey(leftController.up,"w")
screen.onkey(leftController.down,"s")
screen.onkey(rightController.up,'Up')
screen.onkey(rightController.down,'Down')

game_is_on = True
ball.initial_direction_ball()

while game_is_on:

    screen.update()
    sleep(0.019)
    ball.move_ball()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.direction_ball()
    elif ball.distance(leftController.controller[0]) < 60 or ball.distance(leftController.controller[1]) < 60 or ball.distance(leftController.controller[2]) < 60:
        ball.direction_ball()
    elif ball.distance(rightController.controller[0]) < 60 or ball.distance(rightController.controller[1]) < 60 or ball.distance(rightController.controller[2]) < 60:
        ball.direction_ball()

    if ball.xcor() > 500 or ball.xcor() < -500:
        game_is_on = False
        ball.game_over()
        ball.hideturtle()


screen.exitonclick()