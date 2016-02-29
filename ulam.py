
import simple_images
import numpy


def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

def ulam():
    size_x=400
    size_y=400
    img = simple_images.bmpDrawing("ulam.png",size_x,size_y)


    primes = (list(primes_sieve2(size_x*size_y)))


    poziceX=size_x//2
    poziceY=size_y//2

    img.putpixel(poziceX,poziceY,0,0,0) # nastavi stred na cernou
    pocet_kroku=0

    ulamovo_cislo=2
    finish = True
    while finish:
    # for i in range(33):
        for idx,smer in enumerate([(1,0),(0,1),(-1,0),(0,-1)]):
            if idx==2 or idx==0:
                pocet_kroku+=1

            for i in range(pocet_kroku):
                poziceX+=smer[0]
                poziceY+=smer[1]

                if poziceX<0 or poziceY<0 or poziceX>=size_x or poziceY>=size_y:
                    finish=False
                    break
                if ulamovo_cislo in primes:
                    # print("ULAM",ulamovo_cislo,poziceX,poziceY)
                    img.putpixel(poziceX,poziceY,0,0,255)


                ulamovo_cislo+=1

            if not finish:
                break

    img.show()
    img.save()


ulam()