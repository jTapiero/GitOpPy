# Fonction 
'''
une fonction est une suite d operation qu on cherche a appeler plusieur fois dans notre code
en changant ou pas ses parametre
les parametre et le return sont en fonction de ce que veut faire l utilisateur  
important:tjrs definir les fonction  avanr de les appel python compile et execute  en procedurale 
          si la fonction n a pas etait interpreter avant elle ne sera pas reconnu par l interpreteur 
declaration:
    def [NomFct]([param1,param2]):
        cmd         
        cmd
utilisation:
    NomFct(param1,param2)
documentation:
    en dessous de la def de la fonction de trouve un docstring (""" """)
    il sert a la documentation de la fonction 
    la documentation est accesible par help(NomFonction)
    ex: def [NomFct]([param1,param2]):
            """ La fonction sert a 
                param1= default
                outpout
            """
            cmd         
            cmd
return:
    return sert a renvoyer une ou plusieur valeur calculer par une fonction 
    declaration:
        def [NomFct]([param1,param2]):
            cmd         
            return var
            [return var1,var2]
    utilisation:
        var=NomFct()
       [var1,var2=NomFct()]
'''

# signature et parametre
'''
il est important dinstancier les parametre dans lordre de la definition des parametre de la fonction  
    ex: def [NomFct](param1,param2):
        NomFct(value1,value2)
        NomFct(param1=value1,param2=value2)
il est possible d appeler les parametre dans le desordre mais leut nom doivent etre indiquer 
    ex:NomFct(param2=value2,param1=value1)
il est possible de donner une valeur par defaut si les parametre ne sont pas renseigne
    ex:def [NomFct](param1,param2=10):
       NomFct(value1) value sera automatiquement egale a 10
dans dautre language de programation la signature dune fonction est la combinaison
 du nom de lordres et des types de parametre de la fonction 
en python le nom de la fonction est sa signature et une redefinition le la fonction ecrase lancienne def

''' 
# parametre indefini
'''
il est possible de creer une fonction dont on ne connais pas a l avance le nombre de parametre 
les parametreד sont utilisable sous forme de tuple dans la fonction
pour utiliser une liste en tant que liste de parametre
declaration:
    def [NomFct](*param):
utilisation:
    fct(paran1,param2,param3,...)
    def fct(*parametre):
        for elem in parametre
    pour utiliser une liste en tant que liste de parametre on met * dans l appel de la fonction
    fct(*[liste param])

si ont veut aussi ajouter des parametres normale on les places avant le paraametre indetermine
declaration:
    def [NomFct](param1,param2,*param):
utilisation:
    fct(paran1,param2,param3,param4,paran5,param6)
    def fct(param1,param2,*parametre):
        param1
        param2
        for elem in parametre    

'''
# recuperer des parametres nomme dans une liste indefie de parametre en utilisant un dico
'''
def fonction_inconnue(**parametres_nommes):
    parametres_nommes
fonction_inconnue(p=4, j=8)
def fonction_inconnue(*en_liste, **en_dictionnaire):
tous les non nomme se trouveronr en en liste 
tous les nomme se trouveront dans en dictionnaires 
passer un dico en parametre
    parametres = {"sep":" >> ", "end":" -\n"}
    print("Voici", "un", "exemple", "d'appel", **parametres)

'''
# Fonction Lambda
'''
ume fonction lambda est une fonction qui est plus court qu une fonction normale
elle permet de renvoyer un resultat pour un calcul court
le return est automatique 

    declaration:
        var= lambda [arg]:[instruction]
        ex: var=lambda x: x**2
            lmb=lambda x,y: x*y  
    utilisation:
        var2=var(7) ==> var2==49
        var3=lmb(7,5) ==> var3==35
'''
