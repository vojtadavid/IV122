

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


def linreg_():
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
    plt.savefig("linreg.png")


linreg_()