import csv
import matplotlib.pyplot as plt
import numpy as np
import random
import math

data = []
with open('faithful.txt', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar="'")
    for row in spamreader:
        # print(', '.join(row))
        # print((row[0]))
        data.append([float(row[0]),float(row[1])])


# print([d[1] for d in data])
print(data)
plt.plot([d[0] for d in data],[d[1] for d in data],'ro')
plt.show()