import simple_images
import cmath
import math
from numba import jit
import time
import threading




# http://www.freestylersupport.com/wiki/_media/tutorial:sequences_ideas:rainbow_colorwheel.gif
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
def mandelbrot():

    iterations=len(colors)-1

    img = simple_images.bmpDrawing("mandelbrot.png",size,size)

    for i in range(size):
        print(i)
        for j in range(size):
            x = -2 +(3*i/size)
            y = -1 +(2*j/size)
            # print(x,y)

            c = complex(x,y)
            z=complex(0,0)

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
                img.putpixel_3(i,j,colors[iter][0],colors[iter][1],colors[iter][2])

    return img



start = time.time()
img = mandelbrot()
end = time.time()
print("run time",end-start)
img.show()