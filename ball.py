from turtle import Turtle
from random import uniform, random
import math

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")

    def initial_direction_ball(self):
        choose = random()
        direction = uniform(-1, 1) * math.atan(3/5) * (180/math.pi)
        if choose >= 0.5:
            direction += 180
        self.setheading(direction)

    def direction_ball(self):
        d = self.heading()
        p = self.pos()
        if p[0] > 460 or p[0] < -460:
            x = 180
            if p[1]<0:
                x = 540
            self.setheading(x-d)
        elif p[1] > 275 or p[1] < -275:
            self.setheading(360-d)


    def move_ball(self):
        self.forward(10)

    def game_over(self):
        self.goto(0,0)
        self.write('Game Over!', align='center', font=('Courier', 22, 'bold'))