from turtle import*
class Face:
    def __init__(self,x,y):
        self.size=90
        self.coord=(x,y)

    def draw(self):
         self.goHome()
         pensize(3)
         speed(0)
         self.drawOutline()
         self.drawEye(135)
         self.drawEye(45)
         self.drawMouth()

    def goHome(self):
        penup()
        goto(self.coord)

    def drawOutline(self):
        penup()
        forward(self.size)
        left(90)
        pendown()
        circle(self.size)
        self.goHome

    def drawEye(self,turn):

        penup()
        left(turn)
        forward(self.size/2)
        pendown()
        dot(self.size/10)
        self.goHome()
        
f1=Face(0,0)
f1.draw()
done()

