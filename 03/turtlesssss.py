import turtle
import math
import simple_images



class MyTurtle:
    pos_x = 0
    pos_y = 0
    orientation = 0

    isPenUp = False

    img = None


    def __init__(self,filename="turtle.svg"):
        self.img=simple_images.svgDrawing(filename)

    def setheading(self,direction=0):
        self.orientation=0

    def left(self,angle):
        self.orientation = (self.orientation+angle)%360

    def right(self,angle):
        self.orientation = (self.orientation+(360-angle))%360

    def forward(self,distance=100):
        newX = self.pos_x + distance*math.cos(math.radians(self.orientation))
        newY = self.pos_y + distance*math.sin(math.radians(self.orientation))

        if not self.isPenUp:
            self.img.add_line(self.pos_x,self.pos_y,newX,newY)

        self.pos_x=newX
        self.pos_y=newY
    def pos(self):
        return (self.pos_x,self.pos_y)

    def goto(self,x1,y1):
        self.pos_y=y1
        self.pos_x=x1

    def penup(self):
        self.isPenUp = True
    def pendown(self):
        self.isPenUp = False




def n_uhelnik(N=6):

    alex = MyTurtle('uhelnik.svg')

    for i in range(N):
        alex.forward(100)
        alex.left(360/N)



def hvezdicka():
    turtle = MyTurtle('hvezdicka.svg')
    while True:
        turtle.forward(200)
        turtle.left(170)
        if abs(turtle.pos()[0]) < 1 and abs(turtle.pos()[1]) < 1:
            break

hvezdicka()

def pentagram():
    N=5
    alex = MyTurtle('pentagram.svg')
    # wn = turtle.Screen()      # Creates a playground for turtles
    # alex = turtle.Turtle()

    a = 100 # delka strany

    for i in range(N):
        alex.forward(a)
        alex.left(360/N)

    # alex.setheading(0)
    # alex.left(36)
    # alex.forward(a/math.cos(math.radians(36)))

    # wn.mainloop()

hvezdicka()
n_uhelnik()
pentagram()


def sierpinsky(x1=20,y1=990,x2=933,y2=990):
    img = simple_images.svgDrawing("sierpinsky.svg")
    img.add_line(x1,y1,x2,y2)

    stred_zakladna_x = (x1+x2)/2
    stred_zakladna_y = (y1+y2)/2
    delka_strany = math.fabs(x1-x2)
    vyska = math.sqrt(delka_strany**2 - (delka_strany/2)**2)

    img.add_line(x1,y1,stred_zakladna_x,stred_zakladna_y-vyska)
    img.add_line(x2,y2,stred_zakladna_x,stred_zakladna_y-vyska)

    sierpinsky_recursive(img,x1,y1,x2,y2,6)


def sierpinsky_recursive(img,x1=20,y1=20,x2=900,y2=20,N=0):
    print(N)
    if N==0:
        return
    stred_zakladna_x = (x1+x2)/2
    stred_zakladna_y = (y1+y2)/2
    delka_strany = math.fabs(x1-x2)
    vyska = math.sqrt(delka_strany**2 - (delka_strany/2)**2)

    x3 = stred_zakladna_x
    y3 = stred_zakladna_y-vyska

    print(x3,y3)

    stred_vpravo_x = (x2+x3)/2
    stred_vpravo_y = (y2+y3)/2


    stred_vlevo_x = (x1+x3)/2
    stred_vlevo_y = (y1+y3)/2

    img.add_line(stred_zakladna_x,stred_zakladna_y,stred_vlevo_x,stred_vlevo_y)
    img.add_line(stred_zakladna_x,stred_zakladna_y,stred_vpravo_x,stred_vpravo_y)
    img.add_line(stred_vlevo_x,stred_vlevo_y,stred_vpravo_x,stred_vpravo_y)

    sierpinsky_recursive(img,x1,y1,stred_zakladna_x,stred_zakladna_y,N-1)
    sierpinsky_recursive(img,stred_zakladna_x,stred_zakladna_y,x2,y2,N-1)
    sierpinsky_recursive(img,stred_vlevo_x,stred_vpravo_y,stred_vpravo_x,stred_vpravo_y,N-1)


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

    # alex = turtle.Turtle()
    # wn = turtle.Screen()



    distance = 300

    for i in range(3):
        alex.forward(distance)
        alex.left(360/3)


    sierpinsky_turtle_recursice(alex,0,0,distance,3)

    # wn.mainloop()



sierpinsky_turtle()

def koch_rec(mister_turtle,distance,n):

    if n==0:
        mister_turtle.forward(distance)
        return

    koch_rec(mister_turtle,distance/3,n-1)
    mister_turtle.left(60)

    koch_rec(mister_turtle,distance/3,n-1)
    mister_turtle.right(120)
    koch_rec(mister_turtle,distance/3,n-1)
    mister_turtle.left(60)
    koch_rec(mister_turtle,distance/3,n-1)





def koch():
    mister_turtle = MyTurtle('koch.svg')
    # wn = turtle.Screen()
    # mister_turtle.speed(0)
    for i in range(3):
        koch_rec(mister_turtle,500,3)
        mister_turtle.right(120)

    # wn.mainloop()


koch()


def hilbert(rewrite = ['B'],n=5):
    if n==0:
        print(rewrite)
        mister_turtle = MyTurtle('hilbert.svg')
        # wn = turtle.Screen()
        # mister_turtle.speed(0)
        for x in rewrite:

            if x =='+':
                mister_turtle.right(90)
            if x =='-':
                mister_turtle.left(90)
            if x=='A' or x=='B':
                continue
            if x=='F':
                mister_turtle.forward(10)
        # wn.mainloop()
        return
    tmp = []
    for x in rewrite:
        if x=="-" or x=="+" or x=="F":
            tmp.append(x)
        if x=="A":
            tmp+=['-','B','F','+','A','F','A','+','F','B','-']
        if x=="B":
            tmp+=['+','A','F','-','B','F','B','-','F','A','+']

    hilbert(tmp,n-1)


hilbert()


def zanorene_trojuhelniky():
    N = 3
    alex = MyTurtle('zanorene_trojuhelniky.svg')
    # wn = turtle.Screen()  # Creates a playground for turtles
    # alex = turtle.Turtle()
    # alex.speed(0)

    a = 320  # delka strany
    while a!=0:
        a-=20
        for i in range(N):
            alex.forward(a)
            alex.left(360 / N)
        alex.penup()
        alex.goto(alex.pos()[0]+math.cos(math.radians(30))*12 ,alex.pos()[1]+math.sin(math.radians(30))*12)
        alex.pendown()



    # alex.setheading(0)
    # alex.left(36)
    # alex.forward(a / math.cos(math.radians(36)))

    # wn.mainloop()

zanorene_trojuhelniky()


def pootocene_ctverce():
    N = 4
    alex = MyTurtle('ctverce.svg')
    # wn = turtle.Screen()  # Creates a playground for turtles
    # alex = turtle.Turtle()
    # alex.speed(0)

    distance = 400
    for x in range(15):
        for i in range(N):
            alex.forward(distance)
            alex.left(360/N)

        a = 0.9*distance
        b = distance-a
        c = math.sqrt(a**2 + b**2)

        angle = math.asin(a/c)
        print(angle,math.degrees(angle))
        alex.forward(a)
        alex.left(math.degrees(angle))

        distance=c

    # wn.mainloop()


pootocene_ctverce()


def penroose():
    N = 10
    alex = MyTurtle('penrose.svg')
    # wn = turtle.Screen()  # Creates a playground for turtles
    # alex = turtle.Turtle()
    # alex.speed(0)

    heading = 0
    while heading<360:
        distance = 50
        for i in range(N):
            alex.forward(distance)
            alex.left(360 / N)

        heading+=20
        alex.setheading(heading)
    # wn.mainloop()

def divnokruh():
    # wn = turtle.Screen()  # Creates a playground for turtles
    alex = turtle.Turtle()
    alex.speed(0)
    alex = MyTurtle("divnokruh.svg")
    polomer = 300
    posunX = 0
    posunY = 0
    d = polomer
    alex.forward(d * 2)
    while posunX< polomer:

        posunX  += 5


        posunY = math.sqrt(polomer**2 - (polomer-posunX)**2)
        d = math.sqrt(polomer ** 2 - posunY ** 2)

        alex.penup()
        alex.goto(posunX,-posunY)
        alex.pendown()
        alex.forward(d*2)

        alex.penup()
        alex.goto(posunX, +posunY)
        alex.pendown()
        alex.forward(d*2)


        d = math.sqrt(polomer**2-posunY**2)

    alex.goto(polomer,polomer)
    alex.right(90)

    posunX = 0
    posunY = 0
    d = polomer
    alex.forward(d * 2)
    while posunY < polomer:
        posunY += 5

        posunX = math.sqrt(polomer ** 2 - (polomer - posunY) ** 2)
        d = math.sqrt(polomer ** 2 - posunX ** 2)

        alex.penup()
        alex.goto(polomer + posunX, polomer - posunY)
        alex.pendown()
        alex.forward(d * 2)

        alex.penup()
        alex.goto(polomer - posunX, polomer - posunY)
        alex.pendown()
        alex.forward(d * 2)


        d = math.sqrt(polomer ** 2 - posunX ** 2)


    # wn.mainloop()


# divnokruh()
# penroose()

