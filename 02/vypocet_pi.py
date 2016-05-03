
import sys
import math
import random

def compute_pi_gregory_leibniz():
    p = 0
    for k in range(10000):
        # print((4*pow(-1,k))/(2*k+1))
        p+=(4*pow(-1,k))/(2*k+1)
        if k%1000==0:
            print(p,math.fabs(p-math.pi))

    return p

def compute_pi_archimedes():

    a=2*pow(3,1/2)
    b=3

    for i in range(33):
        # print(i,a,math.fabs(a-math.pi),b,math.fabs(b-math.pi))
        a_next=(2*a*b)/(a+b)
        b_next=pow(a_next*b,1/2)

        a=a_next
        b=b_next

def compute_pi_monte_carlo():
    count_in=0
    N = 10000000000
    for i in range(N):
        x = random.random()
        y = random.random()

        if pow(x**2 + y**2,1/2)<1:
            count_in +=1

    print(4*count_in/N)

def compute_pi_BPP():
    p = 0.0
    for n in range(15):
        p+=pow(1/16,n)*( 4/(8*n+1) - 2/(8*n+4) - 1/(8*n+5) - 1/(8*n+6)    )
        # print(p,math.fabs(p-math.pi))
    return p


print(compute_pi_BPP())
print(sys.float_info)
print(math.pi)