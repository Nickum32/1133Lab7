import turtle

def randColor():
    import random
    colorNum=random.randint(1,6)
    colorList=["red", "yellow", "green", "blue", "purple", "orange"]
    return colorList[colorNum]

class Display:
    import turtle
    def __init__(self):
        self.t=turtle.Turtle()
        self.element=[]
        self.scr= self.t.getscreen()
        self.scr.listen()
        self.scr.onclick(self.mouseEvent)
        self.t.penup()
    def mouseEvent(self, x, y):
        self.t.setx(x)
        self.t.sety(y)
        self.t.pendown()
        self.t.begin_fill()
        self.t.color(randColor())
        import random
        radius=random.randint(10,100)
        self.t.circle(radius)
        self.t.end_fill()
        self.t.penup()
        
