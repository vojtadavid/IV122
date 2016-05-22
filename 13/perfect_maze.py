import random
import svgwrite
N=10
maze = [[[True,True,True,True] for j in range(N)] for i in range(N)]
visited = []
def maze_print(maze):
    dwg = svgwrite.Drawing('test.svg', profile='full')
    wall = 40
    # for i in range(N):
    #     for j in range(N):
    #         # print(maze[i][j],end="")\
    #         if i!=N-1 and maze[i][j][2] and maze[i+1][j][0]:
    #             print("_",end="")
    #             dwg.add(dwg.add(dwg.line(( j*maze_wall_size, (i+1)*maze_wall_size), ((j+1)*maze_wall_size,(i+1)*maze_wall_size), stroke=svgwrite.rgb(0, 0, 0, '%'))))
    #         else:
    #             print(" ",end="")
    #         if j!=N-1 and maze[i][j][1] and maze[i][j+1][3]:
    #             print("|",end="")
    #
    #             dwg.add(dwg.add(dwg.line(( (i+1)*maze_wall_size,j*maze_wall_size ), ( (i+1)*maze_wall_size, (j+1)*maze_wall_size, ), stroke=svgwrite.rgb(0, 0, 0, '%'))))
    #         else:
    #             print(" ",end="")
    #     print("")
    # dwg.save()

    dwg.add(dwg.line((0,0),(0,N*wall),stroke=svgwrite.rgb(0, 0, 0, '%')))
    dwg.add(dwg.line((0,0),(N*wall,0),stroke=svgwrite.rgb(0, 0, 0, '%')))
    dwg.add(dwg.line((N*wall,N*wall),(N*wall,0),stroke=svgwrite.rgb(0, 0, 0, '%')))
    dwg.add(dwg.line((N*wall,N*wall),(0,N*wall),stroke=svgwrite.rgb(0, 0, 0, '%')))
    for i in range(N):
        for j in range(N):
            if i!=N-1 and maze[i][j][2] and maze[i+ 1][j][0]:
                # print("line ",i,i+1,i*wall)
                dwg.add(dwg.line( (j*wall,(i+1)*wall) , ((j+1)*wall,(i+1)*wall)  ,stroke=svgwrite.rgb(0, 0, 0, '%')))

            if j!=N-1 and maze[i][j][1] and maze[i][j+1][3]:
                print("line ", i, i + 1, i * wall)
                dwg.add(dwg.line( ((j+1)*wall,i*wall)  ,  ((j+1)*wall,(i+1)*wall) ,stroke=svgwrite.rgb(0, 0, 0, '%')))
    print("dwg save")
    dwg.save()



smery = [(1,0),(0,1),(-1,0),(0,-1)]

def DFS(vertex=(0,0)):
    if vertex==(N-1,N-1):
        return
    visited.append(vertex)
    random.shuffle(smery)
    for dir in smery:
        x = vertex[0]+ dir[0]
        y = vertex[1]+ dir[1]
        if 0<=x<N and 0<=y<N:
            # print(x,y)
            if (x,y) not in visited:
                print(vertex,(x,y),dir)

                if dir==(0,1):
                    maze[vertex[1]][vertex[0]][1]=False
                    maze[y][x][3] = False
                if dir == (1,0):
                    maze[vertex[1]][vertex[0]][2] = False
                    maze[y][x][0] = False
                if dir == (-1,0):
                    maze[vertex[1]][vertex[0]][0] = False
                    maze[y][x][2] = False
                if dir == (0, -1):
                    maze[vertex[1]][vertex[0]][3] = False
                    maze[y][x][1] = False

                # maze_print(maze)
                DFS((x,y))





DFS()


maze_print(maze)
