from Tools.Input import *  
def afficherFlotant(var):
    var=str(var)
    return float(var[:var.index('.')+4])
def afficherFlotant2(var):
    var=str(var)
    partie_entiere, partie_flottante = flottant.var(".")
    return ",".join([partie_entiere, partie_flottante[:3]])


var=inputFloat('Rentrer un Nombre a virgule ')
print(afficherFlotant(var))
def test(*param):
    for elem in param:
        print(elem)


liste=[4,5,6,7,8,9,6,3,5,6,9]
test(*liste)
te=60
def test2(param):
    param+=5
    global te
    te+=5
    print(param)
    print(te)
test2(30)
print(te)


def test3():
    global varb
    varb+=5
    print(varb)
    

varb=312
test3()
print(varb)


