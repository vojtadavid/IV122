
import turtle
import turtlesssss



def grammar(root="A",terminals=[],nonterminals=['A','B'],dictOfRulues={'A':"AB",'B':"A"},n=7):
    output=root

    for i in range(n):
        temp=""
        for x in output:
            if x in nonterminals:
                temp = temp + dictOfRulues[x]
            if x in terminals:
                temp = temp + x

        output=temp

    return output


#cantor dust
# print(grammar("A",[],['A','B'],{ "A":"ABA", "B": "BBB" },3))

def hilbert_curve():
    hilbert = grammar("A", ['F','+','-'], ['A','B'], {"A": "-BF+AFA+FB-","B":"+AF-BFB-FA+"}, 5)

    d = 30
    misterTurtle = turtlesssss.MyTurtle("hilber_curve.svg")

    for x in hilbert:
        if x == 'F':
            misterTurtle.forward(d)
        if x == '-':
            misterTurtle.left(90)
        if x == '+':
            misterTurtle.right(90)

# hilbert_curve()

def dragon_curve():
    dragon = grammar("FX", ['F','+','-'], ['X','Y'], {"X": "X+YF+","Y":"-FX-Y"}, 10)

    d = 30
    misterTurtle = turtlesssss.MyTurtle("dragon_curve.svg")

    for x in dragon:
        if x == 'F':
            misterTurtle.forward(d)
        if x == '-':
            misterTurtle.left(90)
        if x == '+':
            misterTurtle.right(90)

# dragon_curve()

# koch curve
def koch_curve():
    koch = grammar("F",['+','−'],['F'],{ "F" : "F+F−F−F+F"},3)

    d = 30
    misterTurtle = turtlesssss.MyTurtle("koch_curve.svg")

    for x in koch:
        if x == 'F':
            misterTurtle.forward(d)
        if x == '−':
            misterTurtle.left(90)
        if x == '+':
            misterTurtle.right(90)

# koch_curve()

# Pythagoras tree
def tree_I():
    pythagoras_tree = grammar("0",['[',']'],['0','1'],{ "1":"11","0":"1[0]0"},5)

    misterTurtle = turtlesssss.MyTurtle("pythagoras_tree.svg")

    d=30
    misterTurtle.right(90)
    for x in pythagoras_tree:
        if x=='0':
            misterTurtle.forward(d)
        if x=='1':
            misterTurtle.forward(d)
        if x=='[':
            misterTurtle.push()
            misterTurtle.left(45)
        if x == ']':
            misterTurtle.pop()
            misterTurtle.right(45)
tree_I()

def fractal_plant():
    plant = grammar("X",['+','-','[',']'],["X","F"],{"X":"F-[[X]+X]+F[+FX]-X","F":"FF"},4)

    d=30
    misterTurtle = turtlesssss.MyTurtle("fractal_plant.svg")

    for x in plant:
        if x=='F':
            misterTurtle.forward(d)
        if x=='-':
            misterTurtle.left(25)
        if x=='+':
            misterTurtle.right(25)
        if x=='[':
            misterTurtle.push()
        if x==']':
            misterTurtle.pop()

# fractal_plant()

#Sierpinski triangle
def triangle_by_sierpinsky():
    sierp_triangle = grammar("A",['+','-'],['A','B'],{"A":"+B-A-B+", "B":"-A+B+A-"},5)
    print(sierp_triangle)
    d = 30
    misterTurtle = turtlesssss.MyTurtle("sierpinsky_triangle.svg")

    for x in sierp_triangle:
        # print(x)
        if x=='A' or x=='B':
            misterTurtle.forward(d)
        if x=='+':
            misterTurtle.right(60)
            misterTurtle.forward(d)
        if x=='-':
            misterTurtle.left(60)
            misterTurtle.forward(d)


triangle_by_sierpinsky()