class Rectangle():
    def __init__(self,l,w):
        self.length=l
        self.width=w

    def area(self):
        return self.length*self.width

newRect=Rectangle(89,49)
print("Area of the Rectangle is",newRect.area())

