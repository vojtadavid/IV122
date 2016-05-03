import simple_images
import cmath
import math
from numba import jit
import time
import threading
import numpy

colors = []
color = [255,0,0]
for x in [(0,1,0),(-1,0,0),(0,0,1),(0,-1,0),(1,0,0),(0,0,-1)]:
    DIV=4
    for i in range(DIV):
        color[0] += x[0] * (int(255 // DIV))
        color[1] += x[1] * (int(255 // DIV))
        color[2] += x[2] * (int(255 // DIV))
        colors.append(color.copy())
        # print(color)

print(len(colors))
# print(colors)
size = 600

def complex_power(c,n):
    polar = cmath.polar(c)
    # print("r",polar[0],"phi",math.degrees(polar[1]))
    abs_c = (math.sqrt(c.real**2 + c.imag**2))
    # print(abs_c,math.cos(n*polar[1]),math.sin(n*polar[1]))
    abs_c = abs_c**n
    cn = complex(abs_c*math.cos(n*polar[1]),abs_c*math.sin(n*polar[1]))
    print(cn)
    return cn
    # return  complex(polar[0]**n,polar[1]*n)


def f(z):
    return z * z * z - 1.0


def newton():
    eps = 0.0001
    iterations=23

    h = 1e-6

    img = simple_images.bmpDrawing("newton.png",size+1,size+1)
    n=3
    roots = (numpy.roots([1, 0, 0, -1])).tolist()
    # print(roots)

    for i in range(size):
        for j in range(size):
            x = -2.0 +(4.0*i/size)
            y = -2.0 +(4.0*j/size)
            z = complex(x, y)

            iter = 0
            while iter<iterations:
                iter+=1
                dz = (n*pow(z,n-1))
                # print(dz)
                if dz==0:
                    break
                z_new = z - ( pow(z,n)- 1.0)/dz
                # print(abs(z_new - z))

                if abs(z_new - z) < eps:  # stop when close enough to any root
                    break
                z = z_new
            # print(i, j,iter)
            img.putpixel_3(i, j, colors[iter][0], colors[iter][1], colors[iter][2])



    img.show()
    img.save()

newton()

