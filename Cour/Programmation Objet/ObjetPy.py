"""
Definition Class
on  définit leur nom en Camelcase

Instancier objet :
        NomObjet = ConstructeurObj()


class NomdeClasse:
TAb->
     Attribut



"""

"""
Attribut 
"""

"""
Méthode
    condtructeur
    __init__(self):
"""

class Pion1:
    NbAction = 5 #variable partagé a tt la classe
    def __init__(self):
        self.NbAction = 6

pion = Pion1()
print(pion.NbAction)


class Pion:
    def __init__(self):
        self.NbAction = 5
    def Pion(self,NbAction):
        self.NbAction = NbAction

pion = Pion()
print(pion.NbAction)
pion = Pion(5)
print(pion.NbAction)
