class car:

    def __init__(self,brand,color):
        self.brand=brand
        self.color=color

    def display(self):
        print("I have a ",self.brand,"And the color is ",self.color)

object=car("Mercedes","Blue")

object.display()

object1=car("ford","white")

object1.display()

object2=car("Toyota","Black")

object2.display()