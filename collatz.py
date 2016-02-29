import matplotlib.pyplot as plt

def collatz_pocet_kroku(n):
    pocet_kroku = 0
    while(n!=1):
        pocet_kroku+=1
        #print(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n +1
    return pocet_kroku

def collatz_maximum(n):
    maximum = -1
    while(n!=1):
        if n>maximum:
            maximum=n

        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n +1
    return maximum

N= 10000
pocet_kroku_list=[]
maximum_list=[]
for i in range(1,N+1):
    pocet_kroku_list.append(collatz_pocet_kroku(i))
    maximum_list.append(collatz_maximum(i))



plt.plot([i for i in range(1,N+1)], pocet_kroku_list, 'o')
plt.show()

# plt.plot([i for i in range(1,N+1)], maximum_list, 'o')
# plt.show()