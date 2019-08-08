#Class
'''
la programmation oriente objet est un paradigme de programmation
un paradigme de programmation est une maniere de programmer 
la poo consiste a modeliser les differents elements abstrait ou concret d une solution sous formes d objet ayant une relation les un par rapport au autres 
un objet est une entite compose de caracteristique appeler attribut et d action appeler methode 
afin de construire un objet on va creer lui creer un plan modele appeler class  

Afin de créer des objet on créer un modele(Plan) de l objet en question dqns lequelle on va definir 
ses caractèristique(Attributs) et ses Comportement(méthode)
un objet est une instance d une classe (creation d une entite/process/architechture/iteration  basee sur le modele(class)possedant ainsi toutes ses caracteristique)

le Nommage des classes se fait en camelCase(selon eux c est maj a chaque debut de mot)

un constructeur est la fonction permetant d instancier une classe afin de créer un objet
on l apelera donc pour créer un objet
il permetera aussi d executer du code specifique a l objet lors de instanciation:implementation des valeurs dans les attributs,...




#self 
dans la plupart des languages de programation une classe sert a creer un model de l objet qui va servir lors de son instantiation
En Python c PLUS que legerement different 
en python TOUT est objet et meme la CLASSE est un OBJET
ce qui change de bien des manieres sa perception 
#self
un objet (ou occurence/iteration de la classe) est liee(bound) avec son model meme apres son instantiation 
c est a dire que : 1. un l objet de la classe est creer et referer dans la memoire
                   2. les methodes d un objet (instance quelquonqu) sont lieer au methode de l objet de la classe 
                   3. lorsque un objet utilise une methode il fait en fait appel a la methode de l objet de sa classe dans lequelle il se met lui meme en parametre 
                        ex:
                        >>> objet.methode 
                            <bound method NomClasse.methode of <__main__.NomClasse object at 0x00B3F3F0(id memory object)>>
                        >>> NomClasse.methode
                            <function methode at 0x00BA5810(id memory object)>
                        >>> NomClasse.methode(objet,param) == objet.methode(param)



le mot self dans la classe designe en fait l objet(instance de la classe) qui fait appel a lobjet de la classe pour appeler une de ses methode
cela afin de mettre en relation la methode de la classe et l instance qui la appeler 


#cls
du fait que la classe est un objet
on peut definir de par ce fait des methode et attribut specifiaue a la classe 
c est a dire qu il seront accesible par tous les objets de cette classe 
et qu il seront stocke dans l objet de classe ce qui rendrq global tous ces attribut a toutes ces instances 
afin de denomminer une classe dans sa declaration  on peut utiliser le nom de la classe ou le raccourcis cls 
 
exemple:
class NomClasse:
    atribut1=#Attribut de classe
    atribut2=#Attribut de classe
    def __init__(self):
        self.atribut3=
        print(NomClasse.atribut1)

la classe se trouve dans le namespace du fichier dans lequel est charge la classe
on peut acceder au atribut de classe sans acceder par un instance
    ex:
        fct1()
        NomClasse.atribut1


self est un raccourci designant l entite sur lequelle on travaille
cls est un raccourci designant lobjet de la classe























inplementation:

    class NomClasse:
        """docstring
        """
        #lieu ou on definit les attributs 
        #
        #

        def __init__(self):#Constructeur (pour l appeler c est le nom de la classe)
            #on peut aussi les definir ici ou en ajouter ici
            #self.atr=value
            #



    Une classe est un 
    #propriete
    #Constructeur
    #methode
    Declaration
'''

a.b  a est contenue dans b 
Les objets, que j'ai présentés comme des variables, pouvant contenir d'autres variables ou fonctions (que l'on appelle méthodes). On appelle une méthode d'un objet grâce à objet.methode().

Les classes, que j'ai présentées comme des types de données. Une classe est un modèle qui servira à construire un objet ; c'est dans la classe qu'on va définir les méthodes propres à l'objet.