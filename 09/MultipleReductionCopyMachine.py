import numpy as np
import math
import simple_images

salina = 400
griped = 0
size = 800

obrazec_souradnice = [[griped, griped], [griped,griped+salina],[griped+salina,griped+salina],[griped+salina,griped]]
print(obrazec_souradnice)

t = [[0.255,0,0,0.255,0.3726,0.6714],[0.255,0,0,0.255,0.1146,0.2232],[0.255,0,0,0.255,0.6306,0.2232],[0.370,-0.642,0.642,0.370,0.6356,-0.0061]]
# A1 = [[a,b,e],[0,1,0],[0,0,1]]

def print_obrazec(obrazec_souradnice):
    for idx, bod in enumerate(obrazec_souradnice):
        # print(bod, obrazec_souradnice[(idx + 1) % len(obrazec_souradnice)])
        bod2 = obrazec_souradnice[(idx + 1) % len(obrazec_souradnice)]
        bmp.draw_line(int(bod[0] + salina / 2), int(bod[1] + salina / 2), int(bod2[0] + salina / 2), int(bod2[1] + salina / 2))


bmp = simple_images.bmpDrawing("Skaredy_obrazek.bmp",size,size)


print_obrazec(obrazec_souradnice)


#
for i in range(4):
    # i = 2
    A = np.identity(3)

    m = [[t[i][0],t[i][1],t[i][4]],[t[i][2],t[i][3],t[i][5]],[0,0,1]]
    print(m)
    # B = np.dot(A,m)
    # print
    x = [np.dot(m, [x[0], x[1], 0]) for x in obrazec_souradnice]
    print(x)
    print("__________")
    # print_obrazec(x)






bmp.show()