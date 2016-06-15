import simple_images
import math
import random
import sys


def distance_points(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) -(q[0] - p[0]) * (r[1] - q[1])

    if val == 0:
        return 0
    if val > 0:
        return 1
    else:
        return 2

def jarvis_algorithm():
    SIZE = 600
    img = simple_images.bmpDrawing("jarvis.png", SIZE, SIZE)

    N = 20

    points = []

    # nahodne vygeneruj N bodu a vykresli je do platna
    for i in range(N):
        x = int(random.uniform(10, SIZE - 10))
        y = int(random.uniform(10, SIZE - 10))
        points.append([x, y])

    first_point = (SIZE,SIZE)
    for p in points:
        img.put_big_dot_color(p[0],p[1])
        if p[0]<first_point[0]:
            first_point=p


    convex_hull=[]


    p1= first_point
    angle =  math.pi/2

    p_temp = None

    while p_temp!=first_point:


        best_angle = 2*math.pi
        p_temp = None

        for p2 in points:
            if distance_points(p1,p2)==0:
                continue
            if p2 in convex_hull:
                continue

            delta_x = p2[0] - p1[0]
            delta_y = p2[1] - p1[1]
            theta_radians = math.atan2(delta_y, delta_x)
            # print(p1,p2,math.degrees(theta_radians))
            theta_radians = theta_radians - angle
            while (theta_radians < 0):
                theta_radians = theta_radians + math.pi*2

            if theta_radians<best_angle:
                best_angle = theta_radians
                p_temp = p2


        angle = angle + best_angle
        img.draw_line(p1[0],p1[1],p_temp[0],p_temp[1])
        convex_hull.append(p_temp)
        p1 = p_temp

    img.show()
    img.save()


jarvis_algorithm()