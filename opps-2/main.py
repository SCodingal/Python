class Rectangle():
    def __init__(self,l,h):
       self.length=l
       self.height=h

    def rectangle_area(self):
        return self.length*self.height
    
newRectangle = Rectangle(12,10)
print("Dimension of Rectangle - Length : %d Height : %d"% (newRectangle.length, newRectangle.height))
print("Area of Recatangle :", newRectangle.rectangle_area())

newRectangle1 = Rectangle(7,14)
print("Dimension of Rectangle - Length : %d Height : %d"% (newRectangle1.length, newRectangle1.height))
print("Area of Recatangle :", newRectangle1.rectangle_area())

print("%s is a shape"%("rectangle"))