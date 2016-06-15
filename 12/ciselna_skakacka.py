import csv
import queue

mrizka = []
with open('mrizka_4e', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t', quotechar="'")
    for row in spamreader:
        r = []
        for x in row:
            r.append([int(x),False,9999,[]])
        mrizka.append(r)

size_X = len(mrizka[0])
size_Y = len(mrizka)

q = []
q.append((0,0))
mrizka[0][0][2]=0

while len(q)!=0:
    v = q.pop()
    x = v[0]
    y = v[1]
    mrizka[x][y][1]=True

    if mrizka[x][y][0]==0:
        print(mrizka[x][y][3])
        break

    for a in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        tmp_x = x + mrizka[x][y][0]*a[0]
        tmp_y = y + mrizka[x][y][0]*a[1]
        if 0 <= tmp_x < size_X and 0 <= tmp_y < size_Y:

            if mrizka[x][y][2]+1<mrizka[tmp_x][tmp_y][2]:
                q.insert(0, (tmp_x, tmp_y))
                mrizka[tmp_x][tmp_y][2] = mrizka[x][y][2]+1
                mrizka[tmp_x][tmp_y][3]  = mrizka[x][y][3].copy()
                mrizka[tmp_x][tmp_y][3].append([x,y])










