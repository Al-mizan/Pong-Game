from turtle import Turtle

class MiddleBorder(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0,300)
        self.setheading(180)
        self.pendown()
        self.pencolor('white')
        self.pensize(3)
        self.speed('fastest')
        # for i in range(60):
        #     if i%2==0:
        #         self.penup()
        #     else:
        #         self.pendown()
        #     self.forward(10)
        self.goto(0,-300)