import simple_images
import matplotlib
import math

size = 800
img = simple_images.bmpDrawing("bifurcation_diagram_of_logistic_map.png",size,size)


r = r_dolni = 2.8
r_horni = 4

data = []
j=0
while r<r_horni:
    x=0.2

    for i in range(200):
        x_new = r*x*(1-x)
        x=x_new
        if i>100:
            img.putpixel(j,int(x_new*size),0,0,0)

    print(x)
    data.append(x)
    r+=(r_horni-r_dolni)/size
    j+=1



img.show()
img.save()




