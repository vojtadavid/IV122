import pprint

def permutace(seznam = ['A','B','C','D','E']):
    if len(seznam)==1:
        return seznam

    output=[]
    for p in seznam:
        new_seznam = seznam.copy()
        new_seznam.remove(p)
        print(new_seznam)
        for x in permutace(new_seznam):
            output.append(p+x)

    return output


def variace_bezopakovani(seznam = ['A','B','C','D','E'],k=5):
    if len(seznam)==0 or k == 0:
        return [['']]


    output=[]
    k-=1
    for p in seznam:
        new_seznam = seznam.copy()
        new_seznam.remove(p)
        print(new_seznam)
        # if
        for x in variace_bezopakovani(new_seznam,k):
            # print(type(x))
            output.append([p]+x)

    return output

def kombinace(seznam = ['A','B','C','D','E'],k=3):
    output=[]




ll = variace_bezopakovani()
print(ll)
print(len(ll))

