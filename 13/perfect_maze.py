import random
N=10
maze = [[[True,True,True,True] for j in range(N)] for i in range(N)]
visited = []
def maze_print(maze):
    for i in range(N):
        for j in range(N):
            # print(maze[i][j],end="")\
            if i!=N-1 and maze[i][j][2] and maze[i+1][j][0]:
                print("_",end="")
            else:
                print(" ",end="")
            if j!=N-1 and maze[i][j][1] and maze[i][j+1][3]:
                print("|",end="")
            else:
                print(" ",end="")
        print("")






maze_print(maze)


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
                    maze[vertex[0]][vertex[1]][1]=False
                    maze[x][y][3] = False
                if dir == (1,0):
                    maze[vertex[0]][vertex[1]][2] = False
                    maze[x][y][0] = False
                maze_print(maze)
                # DFS((x,y))







DFS()