import simple_images
import random


def factorial(n=5):
    if n==0:
        return 1
    return n*factorial(n-1)

def choose(n,k):
    return (factorial(n))//(factorial(n-k)*factorial(k))


img = simple_images.svgDrawing("pascal.svg",1024,1024)

n=32
y=0
width=8



for i in range(1,n+1):
    pocet_clenu_na_radku=i+1
    zacatek=pocet_clenu_na_radku*width/-2
    for j in range(i+1):
        combn= choose(i,j)
        print(combn,end=" ")
        r = random.randint(0,len(simple_images.colors_SVG)-1)
        img.add_rectangle(zacatek,y,width,width,simple_images.colors_SVG[(combn%7)]) #tyrkysova je krasna barva
        zacatek+=width
    y+=width
    print("")
