def circumference(radius):
    return 2*radius*3.14
r= int(input("Enter a number:"))

print("Circulference of the circle is:", circumference(r))
    
def shutdown(user_input):
    if user_input.lower()=="Yes":
        print("Thank you system is shutting down")

    else:
        print("You can continue with your work")

i=input("Do you want to shutdown the system? yes/no")

shutdown(i)


