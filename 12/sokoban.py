rows = [["#","#","#","#","#","#","#","#"],["#","#","#"," "," ","#","#","#"],["#","#","#","$"," ","#","#","#"],["#"," ","$",".",".","@"," ","#"],["#"," "," "," "," "," "," ","#"],["#","#","#","#","#","#","#","#"]]

def printGamePlan(r):
    for i in range(len(r)):
        for j in range(len(r[0])):
            print(r[i][j],end="")
        print("")


printGamePlan(rows)