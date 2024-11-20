from controller import Controller

class LeftRightController(Controller):
    def __init__(self, position):
        super().__init__()
        y = -20
        if position == 'left':
            x = -465
        else :
            x = 465
        for i in self.controller:
            i.goto(x,y)
            y += 20


    def up(self):
        for turtle in self.controller:
            y = turtle.pos()
            turtle.setpos(y[0], y[1] + 10)

    def down(self):
        for turtle in self.controller:
            y = turtle.pos()
            turtle.setpos(y[0], y[1] - 10)
