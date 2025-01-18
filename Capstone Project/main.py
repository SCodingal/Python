import random

num=random.randint(1,10)

def check():
   loop=True
   turn = 0
   while loop:
       guess=int(input("Enter your guess"))

   
   

       if guess < num:
        print("Your guess is smaller") 
       elif guess > num:
        print("Your guess is bigger") 
       else:
        print("Youe guess is correct") 
        break
     
       turn=turn+1
       print("You have taken",turn,"turns")


print("----------------------------------------------------------------------------------------------------------------")
print("Welcome to the Guess the number game!!!")
print("Instructions: You have to guess the number between the range 1-10")
print("----------------------------------------------------------------------------------------------------------------")
check()
