#La programmation oriente Objet POO
'''
declaration classe:
    class NomClasse:
        """docstring"""
        def __init__(self):#constructeur
            """docstring"""
            self.Atribut1=0
            self.Atribut2=""
            .... 
            
            un constructeur sert a instancier un objet sur le model de la class
            self sert a representer l objet nouvellement creer on va lui affecter des attribut
            un constructeur peut prendre des parametres en plus de self 
            utilisation:
                objet1=NomClasse()
            utilisation Atribut:
                objet.Atribut=
            utilisation Methode:
                objet.Methode()
        
        def methode1(self,param1,param2):#methode
            """docstring"""
            on peut definir autant de methode qu on veut dans une classe 
            on peut acceder a l instance de l objet qui appelle la methode par self 
            on peut acceder a lobjet de la classe par cls
            
        


    Une classe est un 
    #propriete
    #Constructeur
    #methode
    Declaration

utilisation Atribut:
    objet.Atribut=
utilisation Methode:
    objet.Methode()


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
