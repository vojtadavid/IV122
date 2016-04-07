import simple_images
import math
import random


def prusecik_usecek(p1,p2,p3,p4):
    x0 = p1[0]
    y0 = p1[1]
    x1 = p2[0]
    y1 = p2[1]

    x2 = p3[0]
    y2 = p3[1]
    x3 = p4[0]
    y3 = p4[1]

    # print()

    #pokud je primka svisla? x1==x2
    if x0==x1 or x2==x3:
        print("primka je svisla")


    # if ((x0 - x1) * (y2 - y3) - (y0 - y1) * (x2 - x3)) ==0:
    #      return True

    px = ((x0*y1 - y0 * x1) * (x2 - x3) - (x0 - x1) * (x2 * y3 - y2 * x3)) / ((x0 - x1) * (y2 - y3) - (y0 - y1) * (x2 - x3))
    py = ((x0*y1 - y0 * x1) * (y2 - y3) - (y0 - y1) * (x2 * y3 - y2 * x3)) / ((x0 - x1) * (y2 - y3) - (y0 - y1) * (x2 - x3))

    if x2 <= x3 and not (x2 <= px <= x3):
        return  False
    if x3 < x2 and not (x3 < px < x2):
        return False

    if y2 <= y3 and not (y2 <= py <= y3):
        return False
    if y3 < y2 and not (y3 < py < y2):
        return False

    if x0 <= x1 and not (x0 <= px <= x1):
        return False
    if x1 < x0 and not (x1 < px < x0):
        return False

    if y0 <= y1 and not (y0 <= py <= y1):
        return False
    if y1 < y0 and not (y1 < py < y0):
        return False

    return True


def distance_points(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def triangulace_random():
    SIZE = 600
    img = simple_images.bmpDrawing("triangulace.png", SIZE, SIZE)

    N = 10

    points = []

    # points.append([574, 313])
    # points.append([30, 314])
    # points.append([257, 118])
    # points.append([510, 106])
    # points.append([270, 484])
    # points.append([328, 103])
    # points.append([176, 578])
    # points.append([280, 98])
    # points.append([512, 478])
    # points.append([242, 268])


    # nahodne vygeneruj N bodu a vykresli je do platna
    for i in range(N):
        x = int(random.uniform(10,SIZE-10))
        y = int(random.uniform(10,SIZE-10))

        # img.put_big_dot_color(x,y)
        points.append([x,y])


    pridane_usecky = []
    while True:

        candidate_p1 = None
        candidate_p2 = None
        nejmensi_vzdalenost = 2 * SIZE

        #projdi vsechny mozne kombinace bodu
        for p1 in points:
            for p2 in points:
                if p1==p2:
                    continue
                if [p1,p2] in pridane_usecky or [p2,p1] in pridane_usecky:
                    continue
                #zkontroluj zda je usecka kratsi
                if distance_points(p1,p2)<nejmensi_vzdalenost:
                    prusecik_existuje = False
                    # zkontroluj zda by se usecka nekrizila s jiz jinou useckou
                    for usecka in pridane_usecky:
                        p3 = usecka[0]
                        p4 = usecka[1]
                        if prusecik_usecek(p1,p2,p3,p4):
                            prusecik_existuje= True
                            break
                    if prusecik_existuje:
                        continue
                    #zapamatuj si kandidata na nejkratsi usecku
                    nejmensi_vzdalenost = distance_points(p1,p2)
                    candidate_p1 = p1
                    candidate_p2 = p2


        #zakresli a pridej nejkratsi usecku
        if nejmensi_vzdalenost!=2*SIZE:
            print("usecka",candidate_p1[0], candidate_p1[1], candidate_p2[0], candidate_p2[1])
            pridane_usecky.append([candidate_p1, candidate_p2])
            img.draw_line(candidate_p1[0], candidate_p1[1], candidate_p2[0], candidate_p2[1])

            continue

        break

    for p in points:
        img.put_big_dot_color(p[0],p[1])




    img.show()
    img.save()


    # print(prusecik_usecek((30,314),(574,313), (270,484), (242, 268) ))


triangulace_random()