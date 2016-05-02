import numpy as np
import math
import simple_images

def rotation(angle):
    return [[math.cos(angle),-math.sin(angle),0],[math.sin(angle),math.cos(angle),0],[0,0,1]]

def scaling(sx,sy):
    return [[sx,0,0],[0,sy,0],[0,0,1]]
def translation(tx,ty):
    return  [[1,0,tx],[0,1,ty],[0,0,1]]

def shear(k):
    return [[1,k,0],[0,1,0],[0,0,1]]


# vrati N-uhelnik se stranou delky 20
def get_ctverec(strana=20,N=3):
    points = [[math.cos(math.radians(i * (360 / N))) * strana, math.sin(math.radians(i * (360 / N))) * strana] for i in range(N)]
    return points

def ukazka(option=1):
    size=1000
    bmp = simple_images.bmpDrawing("ukazka"+ str(option) + ".png",size+1,size+1)



    # A_list seznam vsech matic jednotlivych transformaci
    A_list = []
    ctverec= None
    pocet_opakovani = 0
    if option==1:
        pocet_opakovani = 15
        ctverec = get_ctverec(50, 4)
        A_list.append(rotation(math.radians(20)))
        A_list.append(scaling(1.1,1.1))
        A_list.append(translation(15,20))

    if option==2:
        pocet_opakovani = 15
        ctverec = get_ctverec(333, 4)
        A_list.append(rotation(math.radians(10)))
        A_list.append(scaling(1.1, 0.8))

    if option==3:
        pocet_opakovani = 3
        ctverec = get_ctverec(50, 4)
        A_list.append(shear(1.6))
        A_list.append(rotation(math.radians(33)))
        A_list.append(scaling(0.9,0.9))
        A_list.append(translation(10,10))


    #vykresleni netrasformovaneho obrazce
    for idx,bod in enumerate(ctverec):
        print(bod,ctverec[(idx+1)%len(ctverec)])
        bod2 = ctverec[(idx+1)%len(ctverec)]
        bmp.draw_line(int(bod[0]+size/2),int(bod[1]+size/2),int(bod2[0]+size/2),int(bod2[1]+size/2))



    #vytvoreni transformacni matice, zaciname s jednotkovou matici
    A = np.identity(3)
    for i in A_list:
        A = np.dot(A,i)
    # print(A)


    for i in range(pocet_opakovani): #celkovy pocet ctvercu ktere se vykresli - vlezou se do obrazku
        new_ctverec = []
        #kazdy bod se transformuje nasobenim transformacni matici
        for bod in ctverec:
            new_ctverec.append(np.dot(A,[bod[0],bod[1],1]))

        #vykresleni transformovanych bodu a jejich spojeni primkami
        for idx, bod in enumerate(new_ctverec):
            print(bod,new_ctverec[(idx+1)%len(new_ctverec)])
            bod2 = new_ctverec[(idx+1)%len(new_ctverec)]
            bmp.draw_line(int(bod[0]+size/2),int(bod[1]+size/2),int(bod2[0]+size/2),int(bod2[1]+size/2))
        ctverec = new_ctverec

    bmp.show()
    bmp.save()

ukazka(3)
