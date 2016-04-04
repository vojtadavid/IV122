

import simple_images
import math


def kruznice(polomer=50,epsilon=0.1):
    size_x=200
    size_y=200
    bmp = simple_images.bmpDrawing("circle.png",size_x,size_y)

    for i in range(size_x):
        for j in range(size_y):
            # print(i-10,j-10)
            x = i-size_x//2
            y = j-size_y//2

            if (x**2 + y**2)<polomer**2 and (x**2 + y**2)>(polomer*(1-epsilon))**2 :
                bmp.putpixel(i,j,0,0,0)
            else:
                bmp.putpixel(i,j,255,255,255)

    bmp.show()

# kruznice()


def kruznice_parametricky(polomer=90):
    size_x=200
    size_y=200
    bmp = simple_images.bmpDrawing("circle_parametricky.png",size_x,size_y)

    # for i in range(size_x):
    #     for j in range(size_y):

    for alfa in range(360):
        alfa_rad = math.radians(alfa)
        print(alfa_rad)

        x = int(polomer*math.cos(alfa_rad))
        y = int(polomer*math.sin(alfa_rad))

        print(x+size_x//2,y+size_x//2)
        bmp.putpixel(x+size_x//2,y+size_y//2,0,0,0)


    bmp.show()

        # print(x,y)


# kruznice_parametricky()


def spiral():
    size_x=200
    size_y=200
    bmp = simple_images.bmpDrawing("circle_parametricky.png",size_x,size_y)

    polomer=33
    for alfa in range(360*5):
        alfa_rad = math.radians(alfa%360)
        print(alfa_rad)

        polomer = math.pow(alfa,1/2)

        x = int(polomer*math.cos(alfa_rad)) + size_x//2
        y = int(polomer*math.sin(alfa_rad)) + size_y//2





        print(x,y)
        bmp.putpixel(x,y,0,0,0)

    bmp.show()
# spiral()


def traingle( strana = 500):
    size = 1000
    bmp = simple_images.bmpDrawing("triangle.png",size,size)

    # y = ax +b
    b = math.sqrt(strana**2 - (strana/2)**2 )
    a = -b/(strana/2)

    for i in range(size):
        for j in range(size):

            x = i-(size//2)
            y = j-(size//2)

            # if y>=0 and y<=x+200 and y<=-x+200 :
            if y>=0 and y<=a*x+b and y<=-a*x+b:
                # print(i,j)
                # print(x,y)
                bmp.putpixel(i,j,0,0,0)



    bmp.show()

# traingle()

def polygon(seznam=[(10, 10), (180, 20), (160, 150), (100, 50), (20, 180)]):
    size=300
    img = simple_images.bmpDrawing("polygon.png",size,size)

    for i in range(len(seznam)):
        j=i+1
        if i==len(seznam)-1:
            j=0
        x1=seznam[i][0]
        y1=seznam[i][1]
        x2=seznam[j][0]
        y2=seznam[j][1]
        # print(x1,y1,x2,y2)

        a = int((y2-y1)/(x2-x1))
        b = int(y1-a*x1)
        print(a,b)
        # y= ax+b

        for l in range(size):
            for m in range(size):
                if math.fabs(m-(a*l+b))<2 :
                    img.putpixel(l,m,0,0,0)




    img.show()


polygon()

def sachovnice_img():
    size=400
    img = simple_images.bmpDrawing("polygon.png",size,size)

    for y in range(size):
            for x in range(size):
                a=0
                if (y//40)%2==0:
                    a=1
                if (x//40)%2==a :
                    img.putpixel(x,y,0,0,0)


    img.show()

# sachovnice_img()


def eclipse(a=80,b=160):
    size = 400
    img = simple_images.bmpDrawing("ellipse.png",size,size)

    for i in range(size):
        for j in range(size):
            # print(i-10,j-10)
            x = i-size//2
            y = j-size//2

            alfa = math.radians(60)
            if ((x*math.cos(alfa)+y*math.sin(alfa))/a)**2 + ((x*math.cos(alfa)-y*math.sin(alfa))/b)**2<=1**2:
            # if (x/a)**2 + (y/b)**2<=1**2:
                img.putpixel(i,j,0,0,0)

    img.show()

# eclipse()

def kruznice():
    size = 400
    img = simple_images.bmpDrawing("ellipse.png",size,size)

    center = size/2
    for i in range(size):
        for j in range(size):
            distance = math.sqrt((math.fabs(i-center))**2 + (math.fabs(j-center))**2)
            # print(distance)
            color = int(math.fabs(0.5*255*(math.cos(0.1*distance))))
            color+=100
            # color = math.fabs(color)
            if color>100:
                # color=0
                print(color)
            img.putpixel(i,j,color,color,color)

    img.show()
# kruznice()