from turtle import Turtle, Screen
from time import sleep

from leftrightcontroller import LeftRightController
from middleborder import MiddleBorder
from ball import Ball

screen = Screen()
screen.setup(width=1000, height=600)
screen.title("Pong Game")
screen.bgcolor('grey20')
screen.colormode(256)


leftController = LeftRightController('left')
rightController = LeftRightController('right')
middleBorder = MiddleBorder()
ball = Ball()

screen.listen()
screen.onkey(leftController.up,"w")
screen.onkey(leftController.down,"s")
screen.onkey(rightController.up,'Up')
screen.onkey(rightController.down,'Down')

screen.update()
sleep(0.09)

screen.exitonclick()