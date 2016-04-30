import simple_images

size = 1000
img = simple_images.bmpDrawing("bifurcation_diagram_of_logistic_map.png",size,size)

x_old = 0.8
# for i in range(size):
i=0.0
while i<size:
    start = 3
    end = 6
    y_scale =1
    r = start + ( (4-start) * i / size)
    x_new = r*x_old*(1-x_old)
    # print(r,x_new)

    # print(x_new*size/y_scale)
    j = x_new*size/y_scale
    if i>0.5 :
        img.putpixel(int(i),int(j),0,0,0)
    x_old = x_new

    i+=0.005

img.show()
img.save()




