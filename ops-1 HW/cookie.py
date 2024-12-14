class cookie:

    def __init__(self,brand,filling):
        self.brand=brand
        self.filling=filling

    def display(self):
        print("I have an/a ",self.brand,"And the filling is ",self.filling)

object=cookie("oreo","milk frosting")

object.display()

object1=cookie("chocolate chip cookie","caramel")

object1.display()

object2=cookie("vanila cookie","nothing")

object2.display()