def tMultiples(x):
    if x%4 == 0:
        if x%100 == 0:
            if x%400 == 0:
                bis = True
                print("L'annnee est bissextile")
            else:
                bis = False
                print("L'annee n'est pas bissextile")
        else:
            bis = True
            print("L'annee est bissextile")
    else:
        bis = False
        print("L'annee n'est pas bissextile")

#    return bis

def Multiples(x):
    if x % 400 == 0 or (x % 100 != 0 and x % 4 == 0):
        bis = True
        print("L'annee est bissextile")
    else:
        bis = False
        print("L'annee n'est pas bissextile")

    return bis
