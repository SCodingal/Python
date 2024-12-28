class Slambook:
    def __init__(self):
        self.book={}

    def add_contact(self,name,favourite):
        if name in self.book.keys():
            print("This  name already existes")

        else:
            self.book[name]=favourite#inserting values into the dictionary 
            print("name added succesfully")

