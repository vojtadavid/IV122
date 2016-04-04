


import simple_images
import math
import random


SIZE = 400

img = simple_images.bmpDrawing("chaos_game_triangle.png",SIZE,SIZE)


N =  4

pointsn = [ [math.cos(math.radians(i*(360/N))),math.sin(math.radians(i*(360/N)))] for i in range(N)]

print(pointsn)


size = 150


points_transform = []
for point in pointsn:
    x = int(point[0]*size)
    y = int(point[1]*size)
    img.put_big_dot(x+SIZE//2,y+SIZE//2)
    points_transform.append([x,y])



img.show()










# size_triangle = 222
#
# Ax= 20
# Ay= 380
#
# Bx=Ax + size_triangle
# By= Ay
#
# Cx = int((Bx-Ax)/2)
# Cy = math.sqrt((size_triangle**2 - (size_triangle/2)**2)
#
# img.put_big_dot(Ax,Ay)
# img.put_big_dot(Bx,By)
# img.put_big_dot(Cx,Cy)
#
#
# img.show()