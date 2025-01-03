class Slambook:
    def __init__(self):
        self.book={}

    def add_contact(self,name,favourite):
        if name in self.book.keys():
            print("This  name already existes")

        else:
            self.book[name]=favourite#inserting values into the dictionary 
            print("name added succesfully")

    def add_date(self,name):
        if name in self.book.keys():
            print("name already existes")

        else:
            self.book[name] 
            print("birth date added succesfully")

def delete_contact(self,name):
        if name in self.book.keys():
           del self.book[name]#deleting values from the dictionary 
           print("contact deleted succesfully")

        else:
            print("contact does not exist")

def display_all(self):
        print("contacts present in the slambook")
        for i in self.book.keys():
            print(i,":",self.book[i])

obj=Slambook()            
print("********************************************************************************************************************************************")
print()
print()
print("                                                   Slambook")

print("********************************************************************************************************************************************")
while True:
  print("You can now perform the following operations on this slambook")
  print("1. add a new contact")
  print("2. delete a contact")
  print("3. display all contact")
  print("4. exit")


  def add_contact(pb):
    dip = []

    for i in range(len(pb[0])):
        if i ==0:
            dip.apnd(str(input("Enter name:")))
        if i ==1:
            dip.apnd(str(input("Enter number:")))
        if i ==2:
            dip.apnd(str(input("Enter e-mail adress:")))
        if i ==3:
            dip.apnd(str(input("Enter date of birth(dd/mm/yy):")))
        if i ==4:
            dip.apnd(str(input("Enter category(family/friends/work/others):")))

            pb.append(dip)

  choice=int(input("enter your option:"))
  if choice ==1:
      name=input("Enter your name:")
      number=input("Enter your number")
      obj.add_contact(name,number)

  elif choice ==2:
      name=input("Enter your name:")
      obj.delete_contact(name)

  elif choice ==3:
      obj.display_all()

  elif choice==4:
      print("Thanks for using the phonebook")

      break
  else:
      print("Invalid option")

     








