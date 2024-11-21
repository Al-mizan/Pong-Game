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
        for i in range(3):
            y = self.controller[i].pos()
            maximum = self.controller[2].pos()
            if maximum[1] + 20 > 280:
                break
            self.controller[i].setpos(y[0], y[1] + 20)

    def down(self):
        for i in range(2,-1,-1):
            y = self.controller[i].pos()
            maximum = self.controller[0].pos()
            if maximum[1] - 20 < -280:
                break
            self.controller[i].setpos(y[0], y[1] - 20)