from turtle import *
import sys
my=Turtle()
a=100
print("Enter amout to move forward:")
moveF=int(input())

for a in range(moveF):
    print("At first",moveF)
    my.forward(moveF)
    a=moveF+100
    my.left(moveF)
    print("After second turn",moveF)
    a=moveF+100
    my.forward(moveF)
    a=moveF+100
    print("After third turn",moveF)
    my.left(moveF)
    a=moveF+100
    print("After fourth turn",moveF)
    my.forward(moveF)
    a=moveF+100
    print(moveF)
    
    if a==500:
        print("Enter 0 to stop")
        stp=int(input())
        if stp==0:
            sys.exit()
    


