import csv
import math


for i in range(1,7):
    filename = ('random'+str(i)+".txt")
    data = None
    with open(filename,newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            data = row

    # print(data)
    cetnost = [0 for i in range(6)]
    for x in row:
        cetnost[int(x)-1]+=1
    # print(len(data),cetnost)

    sum = 0
    sum2 = 0
    for O_i in cetnost:
        E = len(data)/6
        sum  +=((O_i - E)**2)/E
        sum2 +=((O_i - E)**2)/O_i

    chi_squared = sum
    print(filename,"chi squared",chi_squared)






# hm tak to asi nefunguje
def monte_carlo_PI(data):
    in_circle =0
    for idx in range(0,len(data),4):
        # print(idx)
        x=int(data[idx])/6
        y=int(data[idx+1])/6
        z=math.sqrt(x**2 + y**2)
        # print(x,y,z)
        if z <= 1:
            in_circle+=1
    print(in_circle,len(data),in_circle/(len(data)/2),math.fabs(in_circle-math.pi))
