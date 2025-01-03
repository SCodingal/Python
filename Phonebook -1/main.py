class Phonebook:
    def __init__(self):
        self.book={}

    def add_contact(self,name,number):
        if name in self.book.keys():
            print("name already existes")

        else:
            self.book[name]=number#inserting values into the dictionary 
            print("contact added succesfully")

    def update_contact(self,name,number):
        if name in self.book.keys():
            self.book[name]=number#inserting values into the dictionary 
            print("contact updated succesfully")

        else:
            print("contact does not exist")


    def delete_contact(self,name):
        if name in self.book.keys():
           del self.book[name]#deleting values from the dictionary 
           print("contact deleted succesfully")

        else:
            print("contact does not exist")

    def display_all(self):
        print("contacts present in the Phonebook")
        for i in self.book.keys():
            print(i,":",self.book[i])

obj=Phonebook()            
print("********************************************************************************************************************************************")
print()
print()
print("                                                   Phonebook")

print("********************************************************************************************************************************************")
while True:
  print("You can do the following operations")
  print("1. add a contact")
  print("2. update a contact")
  print("3. delete a contact")
  print("4. display all contact")
  print("5. exit")

  choice=int(input("enter your option:"))
  if choice ==1:
      name=input("Enter your name:")
      number=input("Enter your number")
      obj.add_contact(name,number)

  elif choice ==2:
      name=input("Enter your name:")
      number=input("Enter your number")
      obj.update_contact(name,number)

  elif choice ==3:
      name=input("Enter your name:")
      obj.delete_contact(name)

  elif choice ==4:
      obj.display_all()

  elif choice==5:
      print("Thanks for using the phonebook")

      break
  else:
      print("Invalid option")

     








