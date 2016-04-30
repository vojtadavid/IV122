
import turtle



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

#Sierpinski triangle
sierp_triangle = grammar("A",['+','-'],['A','B'],{"A":"+B-A-B+", "B":"-A+B+A-"},15)
# print(sierp_triangle)
alex = turtle.Turtle()
wn = turtle.Screen()
d=5

for x in sierp_triangle:
    # print(x)
    if x=='A' or x=='B':
        alex.forward(d)
    if x=='+':
        alex.left(60)
        alex.forward(d)
    if x=='-':
        alex.right(60)
        alex.forward(d)

wn.mainloop()