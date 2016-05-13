import turtle
import math

def sierpinsky_turtle_recursice(alex,x1,y1,distance,n):
    if n==0:
        return

    alex.penup()
    alex.goto(x1+distance/2,y1)
    alex.setheading(0)
    alex.pendown()
    alex.left(60)

    for i in range(3):
        alex.forward(distance/2)
        alex.left(120)

    vyska = math.sqrt((distance/2)**2 - (distance/4)**2) + y1

    stred_x_vlevo = x1 + distance*0.25

    sierpinsky_turtle_recursice(alex,x1,y1,distance/2,n-1)
    sierpinsky_turtle_recursice(alex,x1+distance/2,y1,distance/2,n-1)
    sierpinsky_turtle_recursice(alex,stred_x_vlevo,vyska,distance/2,n-1)



def sierpinsky_turtle():
    alex = MyTurtle("sierpinsky_turtle.svg")



    distance = 300

    for i in range(3):
        alex.forward(distance)
        alex.left(360/3)


    sierpinsky_turtle_recursice(alex,0,0,distance,3)

    wn.mainloop()



sierpinsky_turtle()