import simple_images
import math
import random


SIZE = 1000
img = simple_images.bmpDrawing("chaos_game_triangle.png",SIZE,SIZE)


N =  3
pointsn = [ [math.cos(math.radians(i*(360/N))),math.sin(math.radians(i*(360/N)))] for i in range(N)]


size = 400

points_transform = []
for point in pointsn:
    x = int(point[0]*size)
    y = int(point[1]*size)
    img.put_big_dot(x+SIZE//2,y+SIZE//2)
    points_transform.append([x+SIZE//2,y+SIZE//2])

print(points_transform)

x = random.randint(0, SIZE-1)
y = random.randint(0, SIZE-1)

for i in range(100000):


    r = random.randint(0,N-1)
    # print(r)
    ABC_x = points_transform[r][0]
    ABC_y = points_transform[r][1]

    img.putpixel(int((x+ABC_x)/2),int((y+ABC_y)/2),0,0,0)

    x = (x+ABC_x)/2
    y = (y+ABC_y)/2


img.show()




