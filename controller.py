from turtle import Turtle


def body():
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape("square")
    new_turtle.color("white")
    new_turtle.speed('fastest')
    return new_turtle


class Controller:

    def __init__(self):
        self.controller = []
        for _ in range(3):
            self.controller.append(body())