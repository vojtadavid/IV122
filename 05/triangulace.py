
import random
import simple_images
import math


def najdi_pruseciky():
    SIZE = 400
    img  = simple_images.bmpDrawing("line_intersection.png",SIZE,SIZE)


    N = 10
    velikost_usecky = 200

    seznam_usecek = []
    n=0
    while(n<N):
        n=n+1
        x_temp = int(random.uniform(10,SIZE-10))
        y_temp = int(random.uniform(10,SIZE-10))

        x0 = int(random.uniform(10,SIZE-10))
        y0 = int(random.uniform(10,SIZE-10))

        x1=-1
        y1=-1

        if (x0-x_temp)==0:
            n=n-1
            continue

        a = (y0-y_temp)/(x0-x_temp)
        b = -a*x0+y0



        # print("y= %d*x + %d" % (a, b))


        # img.put_big_dot(x0, y0)
        # img.put_big_dot(x_temp, y_temp)
        # img.show()

        for x in range(SIZE):
            y = a*x+b
            if y<0 or y>=SIZE:
                continue
            vzdalenost = math.sqrt((x-x0)**2+(y-y0)**2)
            # print(vzdalenost)
            if math.fabs(vzdalenost-velikost_usecky)<2:
                x1=x
                y1=int(y)
                break



        if y1==-1:
            n=n-1
            continue
        print(x0,y0,x1,y1)
        img.draw_line(x0,y0,x1,y1)

        # return

        seznam_usecek.append((x1,y1,x0,y0))






    for usecka1 in seznam_usecek:
        x0 = usecka1[0]
        y0 = usecka1[1]
        x1 = usecka1[2]
        y1 = usecka1[3]
        # print("u1",usecka1)
        for usecka2 in seznam_usecek:
            if usecka1==usecka2:
                continue
            x2 = usecka2[0]
            y2 = usecka2[1]
            x3 = usecka2[2]
            y3 = usecka2[3]
            # print("u2",usecka2)

            a = int((y0 - y1) / (x0 - x1))
            b = int(y1 - a * x1)

            c = int((y2 - y3) / (x2 - x3))
            d = int(y2 - a * x3)

            # print(a,b,c,d)


            if ((x0-x1)*(y2-y3)-(y0-y1)*(x2-x3))==0:
                continue

            px = int(((x0*y1-y0*x1)*(x2-x3)-(x0-x1)*(x2*y3-y2*x3))/((x0-x1)*(y2-y3)-(y0-y1)*(x2-x3)))
            py = int(((x0*y1-y0*x1)*(y2-y3)-(y0-y1)*(x2*y3-y2*x3))/((x0-x1)*(y2-y3)-(y0-y1)*(x2-x3)))

            if x2<x3 and not (x2<px<x3):
                continue
            if x3<x2 and not (x3<px<x2):
                continue

            if y2<y3 and not (y2<py<y3):
                continue
            if y3<y2 and not (y3 < py < y2):
                continue

            if x0 < x1 and not (x0 < px < x1):
                continue
            if x1 < x0 and not (x1 < px < x0):
                continue

            if y0 < y1 and not (y0 < py < y1):
                continue
            if y1 < y0 and not (y1 < py < y0):
                continue


            # print(px,py)
            img.put_big_dot(px,py)

            # if px<0 or py<0 or px>=SIZE  or py>=SIZE:
            #     continue

    img.show()

najdi_pruseciky()








def draw_line(img,x0,y0,x1,y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    x, y = x0, y0
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1
    if dx > dy:
        err = dx / 2.0
        while x != x1:
            img.putpixel(x, y, 0, 0, 0)
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y1:
            img.putpixel(x, y, 0, 0, 0)
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
    img.putpixel(x, y, 0, 0, 0) 


def put_big_dot(img, px,py):
    img.putpixel(px, py, 0, 0, 0)
    img.putpixel(px + 1, py, 0, 0, 0)
    img.putpixel(px - 1, py, 0, 0, 0)
    img.putpixel(px, py + 1, 0, 0, 0)
    img.putpixel(px, py - 1, 0, 0, 0)
    img.putpixel(px + 1, py + 1, 0, 0, 0)
    img.putpixel(px - 1, py - 1, 0, 0, 0)
    img.putpixel(px - 1, py + 1, 0, 0, 0)
    img.putpixel(px + 1, py - 1, 0, 0, 0)


def prusecik_usecek(p1,p2,p3,p4):
    x0 = p1[0]
    y0 = p1[1]
    x1 = p2[0]
    y1 = p2[1]

    x2 = p3[0]
    y2 = p3[1]
    x3 = p4[0]
    y3 = p4[1]


    # a = int((y0 - y1) / (x0 - x1))
    # b = int(y1 - a * x1)
    #
    # c = int((y2 - y3) / (x2 - x3))
    # d = int(y2 - a * x3)

    # print(a, b, c, d)

    # if ((x0 - x1) * (y2 - y3) - (y0 - y1) * (x2 - x3)) ==0:
    #     return False

    px = int(((x0 * y1 - y0 * x1) * (x2 - x3) - (x0 - x1) * (x2 * y3 - y2 * x3)) / (
    (x0 - x1) * (y2 - y3) - (y0 - y1) * (x2 - x3)))
    py = int(((x0 * y1 - y0 * x1) * (y2 - y3) - (y0 - y1) * (x2 * y3 - y2 * x3)) / (
    (x0 - x1) * (y2 - y3) - (y0 - y1) * (x2 - x3)))

    if x2 < x3 and not (x2 < px < x3):
        return  False
    if x3 < x2 and not (x3 < px < x2):
        return False

    if y2 < y3 and not (y2 < py < y3):
        return False
    if y3 < y2 and not (y3 < py < y2):
        return False

    if x0 < x1 and not (x0 < px < x1):
        return False
    if x1 < x0 and not (x1 < px < x0):
        return False

    if y0 < y1 and not (y0 < py < y1):
        return False
    if y1 < y0 and not (y1 < py < y0):
        return False

    return True


def distance_points(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def triangulace_random():
    SIZE = 400
    img = simple_images.bmpDrawing("line_intersection.png", SIZE, SIZE)

    N = 10

    points = []

    for i in range(N):
        x = random.randint(3,SIZE-3)
        y = random.randint(3,SIZE-3)

        img.put_big_dot(x,y)
        points.append([x,y])

    pridane_usecky = []
    while True:
        usecka_pridana = False
        nejmensi_vzdalenost = 99999
        for p1 in points:
            for p2 in points:
                if p1==p2:
                    continue
                if distance_points(p1,p2)<nejmensi_vzdalenost:
                    prusecik_existuje = False
                    for usecka in pridane_usecky:
                        p3 = usecka[0]
                        p4 = usecka[1]
                        if (p1==p3 and p2==p4) or (p1==p4 and p2==p3):
                            prusecik_existuje =True
                            break
                        if prusecik_usecek(p1,p2,p3,p4):
                            prusecik_existuje= True
                            break
                    if prusecik_existuje:
                        breaka
                    nejmensi_vzdalenost = distance_points(p1,p2)
                    pridane_usecky.append([p1,p2])
                    usecka_pridana = True

                    img.draw_line(p1[0],p1[1],p2[0],p2[1])
                    print("NEJMENSI: ",nejmensi_vzdalenost,p1,p2)
                    # img.show()
        if not usecka_pridana:
            break
        # input("press enter")

    img.show()



# triangulace_random()