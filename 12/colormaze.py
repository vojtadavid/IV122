import copy
import svgwrite
# zluta 1
# zelena 2
# modra 3
# cervena 4
# fialova 5
# hneda 6
# prazdne policko 0
# start
# cil

dict = {1:"yellow",2:"green",3:"blue",4:"red",5:"purple",6:"brown",0:"white","end":"gold","start":"white"}


size_X = 4
size_Y = 4
# maze = [[2,1,1,"end"],[1,2,1,0],[2,1,0,1],["start",1,1,2]]
maze = [[1,2,0,"end"],[0,1,2,2],[2,3,3,3],["start",2,3,1]]

# size_X = 6
# size_Y = 6
# maze = [[0,6,1,1,3,"end"],[4,6,2,5,3,1],[1,5,2,3,5,6],[5,3,3,1,2,0],[1,5,3,6,6,1],["start",3,1,6,4,4]]


print(maze)


def print_path(path):
    print(path)
    wall=50
    for l in range(1, len(path)+1):
        dwg = svgwrite.Drawing('color_maze_solution' + str(l)+ '.svg', profile='full')
        dwg.add(dwg.line((0, 0), (0, size_X * wall), stroke=svgwrite.rgb(0, 0, 0, '%')))
        dwg.add(dwg.line((0, 0), (size_X * wall, 0), stroke=svgwrite.rgb(0, 0, 0, '%')))
        dwg.add(dwg.line((size_X * wall, size_X * wall), (size_X * wall, 0), stroke=svgwrite.rgb(0, 0, 0, '%')))
        dwg.add(dwg.line((size_X * wall, size_X * wall), (0, size_X * wall), stroke=svgwrite.rgb(0, 0, 0, '%')))
        for x in range(l):
            i=path[x][0]
            j=path[x][1]
            dwg.add(dwg.rect((j * 50, i * 50), (50, 50), fill=dict[maze[i][j]]))

        dwg.add(dwg.text("start",(10,(size_X-1)*50+25)))
        dwg.save()


def DFS(v,path):
    x=v[0]
    y=v[1]

    path.append((x,y))

    if maze[x][y]=="end":
        pole = [0 for i in range(4)] # pocet barev v bludisti
        for v in path:
            if maze[v[0]][v[1]]=="start" or maze[v[0]][v[1]]=="end":
                continue
            pole[maze[v[0]][v[1]]]+=1

        if len(set(pole[1:]))==1: #zkontroluj zda je kazda barva navstivena stejnekrat
            print_path(path)
            print("END",len(set(pole[1:])),path,pole[1:])

    for a in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        tmp_x = x + a[0]
        tmp_y = y + a[1]
        if 0 <= tmp_x < size_X and 0 <= tmp_y < size_Y and (tmp_x,tmp_y) not in path:
            DFS((tmp_x,tmp_y),copy.deepcopy(path))


path=[]
DFS((3,0),path)



