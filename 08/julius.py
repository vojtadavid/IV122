import simple_images
import cmath
import math
from numba import jit
import time
import threading

colors = []
color = [255,0,0]
for x in [(0,1,0),(-1,0,0),(0,0,1),(0,-1,0),(1,0,0),(0,0,-1)]:
    DIV=10
    for i in range(DIV):
        color[0] += x[0] * (int(255 // DIV))
        color[1] += x[1] * (int(255 // DIV))
        color[2] += x[2] * (int(255 // DIV))
        colors.append(color.copy())
        print(color)

print(len(colors))
# print(colors)
size = 600


@jit
def julia_set():

    iterations=50

    img = simple_images.bmpDrawing("julius.png",size,size)
    # img = [[(0,0,0) for t1 in range(range_i2-range_i1)] for t2 in range(range_j2-range_j1)]

    for i in range(size):
        print(i)
        for j in range(size):
            x = -2 +(4*i/size)
            y = -1.5 +(3*j/size)
            # print(x,y)

            c = complex(-0.13,0.75)
            # c = complex(0, 1)
            z=complex(x,y)

            iter =0
            while True:
                z = z*z + c
                iter +=1
                if iter>=iterations:
                    break
                if math.sqrt(z.real**2 + z.imag**2)>=2:
                    break


            if math.sqrt(z.real**2 + z.imag**2)<2:
                img.putpixel_3(i,j,0,0,0)
            else:
                img.putpixel_3(i,j,255,255,255)

    return img



start = time.time()
img = julia_set()
end = time.time()
print("run time",end-start)
img.show()
img.save()