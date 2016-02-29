from PIL import Image
import random

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
        self.file.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1" >\n')


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

    def add_triangle(self,x1=0,y1=0,x2=50,y2=50,x3=50,y3=0):
        list=[x1,y1,x2,y2,x3,y3,x1,y1]
        self.add_polyline(list)


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

weird_picture()


class bmpDrawing:
    pixels=[]
    # pos = pixel_array_offset + row_size * y + pixel_size * x
    # data[pos:pos+3] = 255, 255, 255
    filename=""
    size_x= 0
    size_y= 0

    img = None

    def __init__(self,filename="easters.png",x=255,y=255):
        self.filename=filename
        self.size_x=x
        self.size_y=y
        self.img = Image.new("RGB", (x, y), (255,255,255))

    def putpixel(self,i, j, r, g, b):
        self.img.putpixel((i,j),(r,g,b))

    def testImage(self):
        for i in range(self.size_x):    # for every pixel:
            for j in range(self.size_y):
                self.img.putpixel((i,j),(i,j,50))
        self.img.show()

    def show(self):
        self.img.show()

    def save(self):
        self.img.save(self.filename)

    # def __del__(self):
        # self.img.save(self.filename)



