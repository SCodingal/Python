import turtle
window=turtle.Screen()
turtle.Screen().bgcolor("Green")
board=turtle.Turtle()
angle=360
n=int(input("enter the number of sides"))

turn=angle/n



for i in range(n):
    board.forward(80)
    board.right(turn)
window.exitonclick()