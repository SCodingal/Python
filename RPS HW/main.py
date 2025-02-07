import random
options=["rock","paper","scissors"]
cc= random.choice(options)

user=input("Enter your choice(rock/paper/scissors)")

if cc =="rock":

    if user == "rock":
        print("Its a Tie")

    elif user == "paper":
        print("player won")

    elif user == "scissors":
         print("computer won")

      
    if cc =="paper":

    elif user == "rock":
        print("computer won")

    elif user == "paper":
        print("Its a tie")

    elif user == "scissors":
         print("computer won")

         if cc =="scissors":

    elif user == "rock":
        print("player won")

    elif user == "paper":
        print("computer won")

    elif user == "scissors":
         print("Its a tie")
