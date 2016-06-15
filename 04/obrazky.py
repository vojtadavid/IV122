

import simple_images
import math


def kruznice(polomer=50,epsilon=0.1):
    SIZE =200
    bmp = simple_images.bmpDrawing("circle.png",SIZE)

    for i in range(SIZE):
        for j in range(SIZE):
            x = i-SIZE//2
            y = j-SIZE//2

            if (x**2 + y**2)<polomer**2 and (x**2 + y**2)>(polomer*(1-epsilon))**2 :
                bmp.putpixel(i,j,0,0,255)

    bmp.show()
    bmp.save()

kruznice()


def kruznice_parametricky(polomer=90):
    SIZE =200
    bmp = simple_images.bmpDrawing("circle.png",SIZE)

    # for i in range(size_x):
    #     for j in range(size_y):

    for alfa in range(360):
        alfa_rad = math.radians(alfa)
        print(alfa_rad)

        x = int(polomer*math.cos(alfa_rad))
        y = int(polomer*math.sin(alfa_rad))

        print(x+SIZE//2,y+SIZE//2)
        bmp.putpixel(x+SIZE//2,y+SIZE//2,0,0,0)


    bmp.show()
    bmp.save()


kruznice_parametricky()


def spiral():
    size_x=400
    size_y=400
    bmp = simple_images.bmpDrawing("circle_parametricky.png",size_x,size_y)

    pocet_otacek = 5

    #alfa_rad je jiz v radianech
    alfa_rad = 0.0
    while (alfa_rad<2*math.pi*pocet_otacek):
        alfa_rad = alfa_rad + 0.0001

        #Archimedean spiral
        #a will turn the spiral, while b controls the distance between successive turnings
        a= 1
        b= 0.1
        polomer = a + b*math.degrees(alfa_rad)
        x = int(polomer*math.cos(alfa_rad)) + size_x//2
        y = int(polomer*math.sin(alfa_rad)) + size_y//2

        bmp.putpixel(x,y,0,0,0)

    bmp.show()
    bmp.save()

spiral()


def triangle( strana = 500):
    size = 1000
    bmp = simple_images.bmpDrawing("triangle.png",size,size)

    # y = ax +b
    b = math.sqrt(strana**2 - (strana/2)**2 )
    a = -b/(strana/2)

    for i in range(size):
        for j in range(size):

            x = i-(size//2)
            y = j-(size//2)

            if y>=0 and y<=-a*x+b and y<=+a*x+b:
                bmp.putpixel(size-i,size-j,0,0,0)



    bmp.show()
    bmp.save()

triangle()

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

        img.draw_line(x1,y1,x2,y2)

        a = int((y2-y1)/(x2-x1))
        b = int(y1-a*x1)

    img.show()
    img.save()


polygon()

def sachovnice_img():
    size=400
    img = simple_images.bmpDrawing("sachovnice.png",size,size)

    for y in range(size):
            for x in range(size):
                i = x - size // 2
                j = y - size // 2
                polomer = math.sqrt(i ** 2 + j ** 2)

                if polomer<150 and polomer>100:
                    a=1
                    if (y//40)%2==0:
                        a=0
                else:
                    a=0
                    if (y//40)%2==0:
                        a=1
                if (x//40)%2==a :
                    img.putpixel(x,y,0,0,0)


    img.show()
    img.save()

sachovnice_img()


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
    img.save()

eclipse()

def kruznice():
    size = 400
    img = simple_images.bmpDrawing("kruznice_asi_barevna.png",size,size)

    center = size//2
    for i in range(size):
        for j in range(size):
            x = i-center
            y = j-center
            distance = math.sqrt((math.fabs(i-center))**2 + (math.fabs(j-center))**2)

            square_size = 100
            if -square_size<=x<=square_size and -square_size<=y<=square_size:
                color = int(math.fabs(0.5 * 255 * (math.cos(0.14 * distance))))
                color += 50
            else:
                color = int(math.fabs(0.5*255*(math.cos(0.1*distance))))
                color+=50

            img.putpixel(i,j,color,color,color)

    img.show()
kruznice()