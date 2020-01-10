import turtle
class Shape(object):
    def __init__(self, x=0, y=0, col="", fill=False):
        #t1 = turtle.Turtle()
        self.xloc = x
        self.yloc = y
        self.color = col
        if fill:
            self.filled = True
        else:
            self.filled = False
    def setFillcolor(self, newcolor):
        self.color = newcolor
    def setFilled(self, boolVal):
        if boolVal:
            self.filled = True
        else:
            self.filled = False
    def isFilled(self, filled):
        return filled
    

class circle(Shape):
    def __init__(self, x=0, y=0, rad=1, fill=False):
        self.xloc = x
        self.yloc = y
        self.radius = rad
        if fill:
            self.filled = True
        else:
            self.filled = False
    def draw(self, t):
        t.setx(self.xloc)
        t.sety(self.yloc)
        if self.filled:
            t.begin_fill()
        t.circle(self.radius)
        if self.filled:
            t.end_fill()
