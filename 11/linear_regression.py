

import csv
import matplotlib.pyplot as plt
import numpy as np
import random
import math

data = []
with open('linreg.txt', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar="'")
    for row in spamreader:
        # print(', '.join(row))
        # print((row[0]))
        data.append([float(row[0]),float(row[1])])


# print([d[1] for d in data])
print(data)
# np.


def dummy_linreg():

    min_SSE = 999999
    best_points = []
    for d1 in data:
        for d2 in data:
            if d1==d2:
                continue
            #y=mx + b
            m = (d2[1]-d1[1])/(d2[0]-d1[0])
            b=d1[1]

            #vypocitej sse pro danou primku
            sum=0
            for d in data:
                sum += (d[1] - (m*d[0] + b))**2
            if sum< min_SSE:
                min_SSE=sum
                best_points=[d1,d2,m,b]


    print(best_points)
    plt.plot([d[0] for d in data],[d[1] for d in data],'ro',[d[0] for d in data],[best_points[2]*d[0]+best_points[3] for d in data],'b')
    plt.show()


def linreg():
    prumer_y = 0
    prumer_x = 0

    for d in data:
        prumer_x += d[0]
        prumer_y += d[1]
    prumer_x = prumer_x / len(data)
    prumer_y = prumer_y / len(data)
    y = np.array([d[1] for d in data])
    print(y)
    std_y = np.std(y)
    x = np.array([d[0] for d in data])
    std_x = np.std(x)
    print(std_x, std_y)

    r = (np.corrcoef([d[0] for d in data], [d[1] for d in data])[1, 0])

    a = r * std_y / std_x
    b = prumer_y - a * prumer_x
    print(a, b)
    plt.plot([d[0] for d in data], [d[1] for d in data], 'ro', [d[0] for d in data], [a * d[0] + b for d in data], 'b')
    plt.show()


def random_data_generator_linear():
    a = random.random()
    b = random.random()
    print("linear: ",a,b)
    # r = np.arange(-4,4,0.01)
    # print(r)
    # plt.plot(r,[pow(math.sqrt(2*math.pi)*0.5,-1)*math.exp(-0.5*x**2)  for x in r],'b')
    # plt.show()
    random_data = []
    for i in range(100):
        x = (random.random()-0.5)*4
        # print(x)
        y = a*x + b

        rand_noise = random.random()*4-2
        y_noise = pow(math.sqrt(2*math.pi)*1,-1)*math.exp(-0.5*y**2)
        # y_noise = y + random.random()*2-1
        # print(y,y_noise)
        random_data.append([x,y])

    # print(random_data)
    plt.plot([d[0] for d in random_data], [d[1] for d in random_data],'.')
    plt.show()

# random_data_generator_linear()

linreg()
