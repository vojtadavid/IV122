import simple_images


def nsd(a, b):
    if b == 0:
        return a
    else:
        return nsd(b, a % b)

size=300

img = simple_images.bmpDrawing("nsd.png", size, size)



results=[0 for i in range(size)]
for i in range(size):
    for j in range(size):
        n = nsd(i, j)
        results[n]+=1
        # print("NSD",i,j,nsd(i,j))
        # low=25
        # if n<255:
        #     print(((n*255)//100))
        #     img.putpixel(i, j, 255-((n*255)//100),255-((n*255)//100),50)
        # else:
        #     img.putpixel(i, j, 255-((n*255)//100), 255-((n*255)//100), 255-((n*255)//100))
        # if n<25:
        #     n=n*10
        # if n < 255:
        #     img.putpixel(i, j, 255-n,255-n,255)
        # else:
        #     img.putpixel(i, j, 255, 255-n, 255-n)

print(results)
