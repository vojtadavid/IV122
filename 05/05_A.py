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
        #bod urcuji smer usecky
        x_temp = int(random.uniform(10,SIZE-10))
        y_temp = int(random.uniform(10,SIZE-10))

        #pevny pocatecni bod usecky
        x0 = int(random.uniform(10,SIZE-10))
        y0 = int(random.uniform(10,SIZE-10))

        x1=-1
        y1=-1

        #kontrola deleni nulou
        if (x0-x_temp)==0:
            n=n-1
            continue

        #vypocet koeficientu smernicove rovnice primky
        a = (y0-y_temp)/(x0-x_temp)
        b = -a*x0+y0

        for x in range(SIZE):
            #dopocitani Y-ove souradnice k X pro usecku
            y = a*x+b
            if y<0 or y>=SIZE:
                continue
            #kontrola delky nove usecky
            vzdalenost = math.sqrt((x-x0)**2+(y-y0)**2)
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


            #kontrola deleni nulou
            if ((x0-x1)*(y2-y3)-(y0-y1)*(x2-x3))==0:
                continue

            #vypocet souradnice pruseciku dvou primek
            px = ((x0*y1-y0*x1)*(x2-x3)-(x0-x1)*(x2*y3-y2*x3))/((x0-x1)*(y2-y3)-(y0-y1)*(x2-x3))
            py = ((x0*y1-y0*x1)*(y2-y3)-(y0-y1)*(x2*y3-y2*x3))/((x0-x1)*(y2-y3)-(y0-y1)*(x2-x3))


            #zkontroluj zda nalezeny prusek lezi na useckach
            #najdi elegantnejsi reseni
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

            #zvyrazni vypocitany prusecik jako velke tecky
            img.put_big_dot(int(px),int(py))


    img.show()
    img.save()

najdi_pruseciky()