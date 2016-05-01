
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
        # print(temp)
        print(i)

    return output



# if "ABAABABAABAABABAABABAABAABABAABAAB" ==grammar():
#     print("OK")
#
#
# if "1111[11[1[0]0]1[0]0]11[1[0]0]1[0]0" == grammar("0",['[',']'],['0','1'],{ "1":"11","0":"1[0]0" },3):
#     print("OK")
#
# #cantor dust
# grammar("A",[],['A','B'],{ "A":"ABA", "B": "BBB" },3)
#
# #kochova curve
# grammar("F",['+','-'],['F'],{ "F":"F+F−F−F+F"},3)

# Pythagoras tree
def tree_I():
    pythagoras_tree = grammar("0",['[',']'],['0','1'],{ "1":"11","0":"1[0]0"},5)
    if "1111[11[1[0]0]1[0]0]11[1[0]0]1[0]0" == pythagoras_tree:
        print("OK")
    print(pythagoras_tree)
    misterTurtle = turtlesssss.MyTurtle()

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


def fractal_plant():
    plant = grammar("X",['+','-','[',']'],["X","F"],{"X":"F−[[X]+X]+F[+FX]−X","F":"FF"},4)
    print(plant)
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
# sierp_triangle = grammar("A",['+','-'],['A','B'],{"A":"+B-A-B+", "B":"-A+B+A-"},15)
# print(sierp_triangle)
# alex = turtle.Turtle()
# wn = turtle.Screen()
# d=5
#
# for x in sierp_triangle:
#     # print(x)
#     if x=='A' or x=='B':
#         alex.forward(d)
#     if x=='+':
#         alex.left(60)
#         alex.forward(d)
#     if x=='-':
#         alex.right(60)
#         alex.forward(d)
#
# wn.mainloop()