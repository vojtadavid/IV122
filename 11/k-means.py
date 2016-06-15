import csv
import matplotlib.pyplot as plt
import numpy as np
import random
import math


# http://www.naftaliharris.com/blog/cluster-lib/generate.js
def smiley(n):
    data = [ () for i in range(n)]

    i = 0
    while(i < n):
        x = random.random() * 200 - 100
        y = random.random() * 200 - 100

        # Smiley params
        a = 6*2
        b = 18
        d = 4*2
        c = 0.15
        C = (c - a / (b*b))

        # The border
        if(x*x + y*y < 1000 and x*x + y*y > 810):
            data[i] = (x,y)
            i += 1
        # Left eye
        elif((x+8)*(x+8) + (y-8)*(y-8) < 10):
            data[i] = (x, y)
            i += 1

        # Right eye
        elif ((x - 8) * (x - 8) + (y - 8) * (y - 8) < 10):
            data[i] = (x, y)
            i += 1

        # Smile
        elif((0 < x < -10) and ( -10 < y < 10)):
            print((x,y))
            data[i] = (x, y)
            i += 1


    return data

def uniform(n):
    data = [ () for i in range(n)]

    i = 0
    while (i < n):
        x = random.random() * 400 - 200
        y = random.random() * 400 - 200
        data[i] = [x, y,0]
        i+=1

    return data

def distance(a,b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 )

data = uniform(800)

print(len(data),data)


K = 4
# b: blue
# g: green
# r: red
# c: cyan
# m: magenta
# y: yellow
# k: black
# w: white

colors = ['b','g','r','c','m','y','k']
centroids = [ [random.random() * 200 - 100,random.random() * 200 - 100,i] for i in range(K) ]
print(centroids)

clusters = [[] for i in range(K)]





iter=0
while True:
    for c in centroids:
        plt.plot(c[0], c[1], colors[c[2]] + "h", markersize=15)

    for d in data:
        plt.plot(d[0], d[1], colors[d[2]] + "o")
    plt.savefig("kmeans"+ str(iter) + ".png")
    plt.clf()

    iter += 1


    for idx,d in enumerate(data):

        nejblizsi_centroid = None
        nejmensi_vzdalenost = 9999
        for c in centroids:
            if distance(d,c)<nejmensi_vzdalenost:
                nejblizsi_centroid = c
                nejmensi_vzdalenost = distance(d,c)
        data[idx][2]=nejblizsi_centroid[2]
        clusters[nejblizsi_centroid[2]].append(d)


    centroids_zmena = False
    for idx,c in enumerate(clusters):
        # print(c)
        x = sum([x[0] for x in c])/len(c)
        y = sum([x[1] for x in c]) / len(c)

        if math.fabs(x-centroids[idx][0])>0.5 or math.fabs(y-centroids[idx][1])>0.5:
            centroids_zmena = True

        centroids[idx][0] = x
        centroids[idx][1] = y

    if not centroids_zmena:
        print("quit you should")
        break

    print(iter)






plt.figure()
for c in centroids:
    plt.plot(c[0],c[1],colors[c[2]]+"h",markersize=15)

for d in data:
    plt.plot(d[0], d[1], colors[d[2]] + "o" )
plt.savefig("kmeans"+ str(iter) + ".png")
#
#
# print("OK")
# for idx,d in enumerate(data):
#
#     nejblizsi_centroid = None
#     nejmensi_vzdalenost = 9999
#     for c in centroids:
#         if distance(d,c)<nejmensi_vzdalenost:
#             nejblizsi_centroid = c
#             nejmensi_vzdalenost = distance(d,c)
#     data[idx][2]=nejblizsi_centroid[2]
#     clusters[nejblizsi_centroid[2]].append(d)
#
# print("OK")
# for d in data:
#     plt.plot(d[0], d[1], colors[d[2]] + "o" )
# for c in centroids:
#     plt.plot(c[0],c[1],colors[c[2]]+"h",markersize=15)
# plt.show()