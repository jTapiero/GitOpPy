#La programmation oriente Objet POO
'''
la programmation oriente objet est un paradigme de programmation
un paradigme de programmation est une maniere de programmer 
la poo consiste a modeliser les differents elements abstrait ou concret d une solution sous formes d objet ayant une relation les un par rapport au autres 
un objet est une entite compose de caracteristique appeler attribut et d action appeler methode 
afin de construire un objet on va creer lui creer un plan modele appeler class  

    Une classe est un 
    #propriete
    #Constructeur
    #methode
    Declaration



'''
#Objet
'''
    instanciation
    utilisation 
'''






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
