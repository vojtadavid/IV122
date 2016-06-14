from PIL import Image
import random
import math

colors_SVG=[ "aliceblue" , "aqua" , "aquamarine" , "azure" , "beige" ,
"bisque" , "black" , "blanchedalmond" , "blue" , "blueviolet" , "brown" ,
 "burlywood" ,"cadetblue" , "chartreuse" , "chocolate" , "coral" , "cornflowerblue" ,
 "cornsilk" , "crimson" , "cyan" , "darkblue" , "darkcyan" , "darkgoldenrod" ,
 "darkgray" , "darkgreen" , "darkgrey" , "darkkhaki" , "darkmagenta" , "darkolivegreen" ,
 "darkorange" , "darkorchid" , "darkred" , "darksalmon" , "darkseagreen" , "darkslateblue" ,
 "darkslategray" , "darkslategrey" , "darkturquoise" , "darkviolet" , "deeppink" , "deepskyblue" ,
 "dimgray" , "dimgrey" , "dodgerblue" , "firebrick" , "forestgreen" ,
 "fuchsia" , "gainsboro" ,  "gold" , "goldenrod" , "gray" ,
 "grey" , "green" , "greenyellow" , "honeydew" , "hotpink" , "indianred" ,
 "indigo" , "ivory" , "khaki" , "lavender" , "lavenderblush" , "lawngreen" ,
 "lemonchiffon" , "lightblue" , "lightcoral" , "lightcyan" , "lightgoldenrodyellow" , "lightgray" ,
 "lightgreen" , "lightgrey" , "lightpink" , "lightsalmon" , "lightseagreen" , "lightskyblue" ,
 "lightslategray" , "lightslategrey" , "lightsteelblue" , "lightyellow" , "lime" ,
 "limegreen" , "linen" , "magenta" , "maroon" , "mediumaquamarine" , "mediumblue" ,
 "mediumorchid" , "mediumpurple" , "mediumseagreen" , "mediumslateblue" , "mediumspringgreen" , "mediumturquoise" ,
 "mediumvioletred" , "midnightblue" , "mintcream" , "mistyrose" , "moccasin" , "navy" , "oldlace" , "olive" , "olivedrab" , "orange" , "orangered" ,
 "orchid" , "palegoldenrod" , "palegreen" , "paleturquoise" , "palevioletred" , "papayawhip" ,
 "peachpuff" , "peru" , "pink" , "plum" , "powderblue" , "purple" ,
 "red" , "rosybrown" , "royalblue" , "saddlebrown" , "salmon" , "sandybrown" ,
 "seagreen" , "seashell" , "sienna" , "silver" , "skyblue" , "slateblue" ,
 "slategray" , "slategrey" , "snow" , "springgreen" , "steelblue" , "tan" ,
 "teal" , "thistle" , "tomato" , "turquoise" , "violet" , "wheat" , "yellow" , "yellowgreen" ]

class svgDrawing:
    file = None


    default_color="black"
    default_width=0.8

    def __init__(self,filename="test_svg_image.svg",width=100,height=100):
        self.file = open(filename,"w")
        self.file.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
        self.file.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n')
        self.file.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="1000" height="1000">\n')


    def add_line(self,x1=0,y1=0,x2=120,y2=120,color=default_color,width=default_width):
        self.file.write('<line x1="' + str(x1) + '" y1="'+str(y1)+'" x2="'+str(x2)+'" y2="'+str(y2)+'" style="stroke:'+color+';stroke-width:'+str(width)+'"/>\n')

    def add_circle(self,cx=50,cy=50,r=25,color=default_color,width=default_width):
        self.file.write('<circle cx="'+ str(cx)+ '" cy="'+ str(cy)+'" r="'+ str(r)+'" stroke="'+color+'" stroke-width="'+ str(width)+'" fill="none" />\n')

    def add_polyline(self,polyList=[0,40,40,40,40,80,80,80,80,120,120,120,120,160],color=default_color,width=default_width):
        points=" "
        for idx,i in enumerate(polyList):
            if idx%2==0:
                points += str(i) + ","
            else:
                points += str(i) + " "

        # print(points)
        self.file.write('<polyline points="'+ points + '" style="fill:none;stroke:'+color+';stroke-width:'+str(width)+'" />')

    def group_start(self):
        self.file.write('<g>')
    def group_end(self):
        self.file.write('</g>')

    def __del__(self):
        self.file.write('</svg>\n')

    def add_rectangle(self,x1=0,y1=0,width=150,height=150,color="black"):
        self.file.write('<rect x="'+str(x1)+'" y="'+str(y1)+'" width="'+ str(width) +'" height="'+str(height)+'" style="fill:'+color+';stroke:'+ color +';stroke-width:'+ str(self.default_width) +'" />')


def weird_picture():
    img = svgDrawing("weird.svg")

    img.group_start()

    img.add_line(-100,0,100,0)
    img.add_line(0,100,0,-100)

    for i in range(1,10):
        start=(i*10,i*10)
        for idx,kvadrant in enumerate([(1,0),(0,1),(-1,0),(0,-1)]):
            # print(start[0]*kvadrant[0],start[1]*kvadrant[1])
            e = 100 - i*10
            end1=(e*kvadrant[1],e*kvadrant[0])
            end2=(-e*kvadrant[1],-e*kvadrant[0])


            r = random.randint(0,len(colors_SVG)-1)
            img.add_line(start[0]*kvadrant[0],start[1]*kvadrant[1],end1[0],end1[1],colors_SVG[r])

            r = random.randint(0,len(colors_SVG)-1)
            img.add_line(start[0]*kvadrant[0],start[1]*kvadrant[1],end2[0],end2[1],colors_SVG[r])

            # img.add_line(start[0],start[1],end1[0],end1[1])
            # img.add_line(start[0],start[1],end2[0],end2[1])

    img.group_end()

# weird_picture()


class bmpDrawing:
    pixels=[]
    # pos = pixel_array_offset + row_size * y + pixel_size * x
    # data[pos:pos+3] = 255, 255, 255
    filename=""
    size_x= 0
    size_y= 0

    color_pointer = 0

    # ccolors = [(0,0,0),(255,255),(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255),(255,0,255),(192,192,192),(128,128,128),(128,0,0),(128,128,0),(0,128,0),(128,0,128),(0,128,128),(0,0,128)]
    colors = [("Black", (0, 0, 0)),
              ("Red", (255, 0, 0)),
              ("Lime", (0, 255, 0)),
              ("Blue", (0, 0, 255)),
              ("Yellow", (255, 255, 0)),
              ("CyanAqua", (0, 255, 255)),
              ("Magenta", (255, 0, 255)),
              ("Silver", (192, 192, 192)),
              ("Gray", (128, 128, 128)),
              ("Maroon", (128, 0, 0)),
              ("Olive", (128, 128, 0)),
              ("Green", (0, 128, 0)),
              ("Purple", (128, 0, 128)),
              ("Teal", (0, 128, 128)),
              ("Navy", (0, 0, 128))]

    img = None

    def __init__(self,filename="easters.png",x=255,y=255):
        self.filename=filename
        self.size_x=x
        self.size_y=y
        self.img = Image.new("RGB", (x+1, y+1), (255,255,255))

    def putpixel(self,i, j, r, g, b):
        # print("putpixel",i,j,self.size_y - j)
        self.img.putpixel((i,self.size_y - j),(r,g,b))

    def putpixel_3(self,i, j, r, g, b):
        # print("putpixel", i, j)
        self.img.putpixel((i,j),(r,g,b))

    def putpixel_2(self, i, j, color):
        self.img.putpixel((i, self.size_y - j), color)

    def testImage(self):
        for i in range(self.size_x):    # for every pixel:
            for j in range(self.size_y):
                self.putpixel(i,j,i,j,50)
        self.img.show()

    def show(self):
        self.img.show()

    def save(self):
        self.img.save(self.filename)

    def put_big_dot(self, px, py):
        self.putpixel(px, py, 0, 0, 0)
        self.putpixel(px + 1, py, 0, 0, 0)
        self.putpixel(px - 1, py, 0, 0, 0)
        self.putpixel(px, py + 1, 0, 0, 0)
        self.putpixel(px, py - 1, 0, 0, 0)
        self.putpixel(px + 1, py + 1, 0, 0, 0)
        self.putpixel(px - 1, py - 1, 0, 0, 0)
        self.putpixel(px - 1, py + 1, 0, 0, 0)
        self.putpixel(px + 1, py - 1, 0, 0, 0)

    def put_big_dot_color(self,px,py):

        print("DOT",px,py,self.colors[self.color_pointer%len(self.colors)][0])

        for d in [(1,0),(0,1),(1,1),(-1,-1),(1,-1),(-1,1),(-1,0),(0,-1),(0,0), (2,0),(0,2),(-2,0),(0,-2)]:
            x= px + d[0]
            y= py + d[1]
            self.putpixel_2(x,y,self.colors[self.color_pointer%len(self.colors)][1])

        self.color_pointer = self.color_pointer + 1
        # self.putpixel(px, py, 0, 0, 0)
        # self.putpixel(px + 1, py, 0, 0, 0)
        # self.putpixel(px - 1, py, 0, 0, 0)
        # self.putpixel(px, py + 1, 0, 0, 0)
        # self.putpixel(px, py - 1, 0, 0, 0)
        # self.putpixel(px + 1, py + 1, 0, 0, 0)
        # self.putpixel(px - 1, py - 1, 0, 0, 0)
        # self.putpixel(px - 1, py + 1, 0, 0, 0)
        # self.putpixel(px + 1, py - 1, 0, 0, 0)


    def draw_line(self, x0, y0, x1, y1):
        # print(x0, y0, x1, y1)
        dx = math.fabs(x1 - x0)
        dy = math.fabs(y1 - y0)
        x = x0
        y = y0
        sx = -1 if x0 > x1 else 1
        sy = -1 if y0 > y1 else 1

        if dx > dy:
            err = dx / 2.0
            while x != x1:
                self.putpixel(x, y, 0, 0, 0)
                err -= dy
                if err < 0:
                    y += sy
                    err += dx
                x += sx
        else:
            err = dy / 2.0
            while y != y1:
                self.putpixel(x, y, 0, 0, 0)
                err -= dx
                if err < 0:
                    x += sx
                    err += dy
                y += sy
        self.putpixel(x, y, 0, 0, 0)

    # def __del__(self):
        # self.img.save(self.filename)



