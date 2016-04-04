from fractions import Fraction
import math


def mocnina(x,y):
    result = 1
    for i in range(y):
        result *=x
    return result

def odmocnina_bisekce(x=2,y=2):


    eps=0.000001
    a=0
    b=x
    stred=(a+b)/2

    if pow(a,y)-x==0:
            return a
    if pow(b,y)-x==0:
            return b

    while math.fabs(a-b)>eps:
    # for i in range(10):
        if pow(stred,y)-x==0:
            return stred
        # print(a,b,stred)
        if (pow(a,y)-x)*(pow(stred,y)-x)<0:
            b=stred
        if (pow(stred,y)-x)*(pow(b,y)-x)<0:
            a=stred
        stred=(a+b)/2
        # print(a,b)

    return stred

def odmocnina_newton(x=2,y=2):

    der = y-1
    x_old = x - ( pow(x,y) - x )/(y*pow(x,y-1))

    for i in range(10):

        x_new = x_old - (pow(x_old,y)-x)/(y*pow(x_old,y-1))
        x_old = x_new

        print(x_old,x_new)


# print(Fraction(math.pi))

# f = Fraction(math.pi).limit_denominator(100000)
# print(f.denominator,f.numerator)

# powerof()

# print(odmocnina_bisekce())
print(odmocnina_newton())
print(pow(2,1/2))