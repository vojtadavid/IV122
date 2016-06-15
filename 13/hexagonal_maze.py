import random
import svgwrite
import math
N=5

N_sloupce = 6
N_radky = 6*2

maze = [[[True,True,True,True,True,True] for j in range(N_sloupce)] for i in range(N_radky)]

visited = []

# 0 doprava dolu
# 1 dolu
# 2 doleva dolu
# 3 doleva nahoru
# 4 nahoru
# 5 doprava nahoru
directions_sude = [(1,0),(2,0),(+1,-1),(-1,-1),(-2,0),(-1,0)]
directions_liche = [(1,1),(2,0),(+1,0),(-1,0),(-2,0),(-1,1)]



def print_maze():
    dwg = svgwrite.Drawing('hexagonal_maze.svg', profile='full')
    a=40
    y = math.sqrt(a ** 2 - (a / 2) ** 2)
    hex = [(a, 0), (a / 2, y), (-a / 2, y), (-a, 0), (-a / 2, -y), (a / 2, -y), (a, 0)]  # vrcholy hexagonu


    for i in range(N_radky):
        shift_y =(i*y) +50

        # vykresleni hexagonu v sudem sloupci sloupci
        if i%2 == 0:
            for j in range(N_sloupce):

                shift_x = j*3*a + 50
                dwg.add(dwg.circle((shift_x,shift_y),3))

                for idx in range(len(hex) - 1):
                    x1 = hex[idx][0] + shift_x
                    y1 = hex[idx][1] + shift_y
                    x2 = hex[idx + 1][0] + shift_x
                    y2 = hex[idx + 1][1] + shift_y

                    dir = directions_sude[idx % 6]

                    #pridani sten uvnitr bludiste
                    if 0 <= i + dir[0] < N_radky and 0 <= j + dir[1] < N_sloupce and (not maze[i][j][idx]) and (not maze[i + dir[0]][j + dir[1]][(idx + 3) % 6]):
                        print((i,j),(i + dir[0],j + dir[1]),idx)
                        dwg.add(dwg.line((x1, y1), (x2, y2), stroke=svgwrite.rgb(0, 0, 0, '%')))

                    #pridani okraju bludiste
                    if i == 0 and (idx in [3,4,5]):
                        dwg.add(dwg.line((x1, y1), (x2, y2), stroke=svgwrite.rgb(0, 0, 0, '%')))

                    if i%N_radky%2 ==0 and i == N_radky-2 and (idx in [1]):
                        dwg.add(dwg.line((x1, y1), (x2, y2), stroke=svgwrite.rgb(0, 0, 0, '%')))
                    if j==0 and (idx in [2,3]):
                        dwg.add(dwg.line((x1, y1), (x2, y2), stroke=svgwrite.rgb(0, 0, 0, '%')))

                    if i == N_radky -1 and idx in [0,1,2]:
                        dwg.add(dwg.line((x1, y1), (x2, y2), stroke=svgwrite.rgb(0, 0, 0, '%')))


        # vykresleni hexagonu v lichem sloupci
        if i % 2 == 1:
            for j in range(N_sloupce):
                shift_y = (i * y) + 50
                shift_x = j * 3 * a + 50 + 3*a/2

                dwg.add(dwg.circle((shift_x, shift_y), 3))

                for idx in range(len(hex) - 1):
                    x1 = hex[idx][0] + shift_x
                    y1 = hex[idx][1] + shift_y
                    x2 = hex[idx + 1][0] + shift_x
                    y2 = hex[idx + 1][1] + shift_y

                    dir = directions_liche[idx % 6]

                    if 0 <= i + dir[0] < N_radky and 0 <= j + dir[1] < N_sloupce and (not maze[i][j][idx]) and (not maze[i + dir[0]][j + dir[1]][(idx + 3) % 6]):
                        print((i,j),(i + dir[0],j + dir[1]),idx)
                        dwg.add(dwg.line((x1, y1), (x2, y2), stroke=svgwrite.rgb(0, 0, 0, '%')))

                    #pridani okraju bludiste
                    if i==1 and idx==4:
                        dwg.add(dwg.line((x1, y1), (x2, y2), stroke=svgwrite.rgb(0, 0, 0, '%')))

                    if N_radky%2==1 and i==N_radky-2 and idx in [1]:
                        dwg.add(dwg.line((x1, y1), (x2, y2), stroke=svgwrite.rgb(0, 0, 0, '%')))

                    if i == N_radky - 1 and idx in [0,1,2]:
                        dwg.add(dwg.line((x1, y1), (x2, y2), stroke=svgwrite.rgb(0, 0, 0, '%')))

                    if j== N_sloupce -1 and idx in [0,5]:
                        dwg.add(dwg.line((x1, y1), (x2, y2), stroke=svgwrite.rgb(0, 0, 0, '%')))


    print("dwg save")
    dwg.save()



# 0 doprava dolu
# 1 dolu
# 2 doleva dolu
# 3 doleva nahoru
# 4 nahoru
# 5 doprava nahoru
def DFS(vertex=(0,0)):
    visited.append(vertex)

    if vertex==(N_radky-1,N_sloupce-1):
        return

    directions = None
    if vertex[0]%2==0:
        directions=directions_sude[:]
    else:
        directions=directions_liche[:]


    random.shuffle(directions)

    for dir in directions:
        x = vertex[0]+ dir[0]
        y = vertex[1]+ dir[1]

        if 0<=x<N_radky and 0<=y< N_sloupce and (x,y) not in visited:

            if dir in [(-1,0)] and vertex[0]%2==0:
                maze[vertex[0]][vertex[1]][5] = False
                maze[x][y][2] = False
                print(vertex,(x,y),"doprava nahoru")

            if dir in [(1, 0)] and vertex[0]%2==0:
                maze[vertex[0]][vertex[1]][0] = False
                maze[x][y][3] = False
                print(vertex,(x, y), "doprava dolu")

            if dir in [(-1,-1)] and vertex[0]%2==0:
                maze[vertex[0]][vertex[1]][3] = False
                maze[x][y][0] = False
                print(vertex,(x, y), "doleva nahoru")

            if dir in [(1, -1)] and vertex[0]%2==0:
                maze[vertex[0]][vertex[1]][2] = False
                maze[x][y][5] = False
                print(vertex,(x, y), "doleva dolu")



            if dir in [(-1, 1)] and vertex[0] % 2 == 1:
                maze[vertex[0]][vertex[1]][5] = False
                maze[x][y][2] = False
                print(vertex, (x, y), "doprava nahoru")

            if dir in [(1, 1)] and vertex[0] % 2 == 1:
                maze[vertex[0]][vertex[1]][0] = False
                maze[x][y][3] = False
                print(vertex,(x, y), "doprava dolu")

            if dir in [(-1, 0)] and vertex[0] % 2 == 1:
                maze[vertex[0]][vertex[1]][3] = False
                maze[x][y][0] = False
                print(vertex,(x, y), "doleva nahoru")

            if dir in [(1, 0)] and vertex[0] % 2 == 1:
                maze[vertex[0]][vertex[1]][2] = False
                maze[x][y][5] = False
                print(vertex,(x, y), "doleva dolu")


            if dir == (-2, 0):
                maze[vertex[0]][vertex[1]][4] = False
                maze[x][y][1] = False
                print(vertex,(x, y), "nahoru")

            if dir == (2, 0):
                maze[vertex[0]][vertex[1]][1] = False
                maze[x][y][4] = False
                print(vertex, (x, y), "dolu")

            DFS((x,y))





DFS()
print_maze()