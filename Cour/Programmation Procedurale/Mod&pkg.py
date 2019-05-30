#Module 
'''
un module python est un emsenble de code(objet,fonction,variable....)
se trouvent sur une autre page et dont on veut utiliser les ressources aui se trouvent a l interieur
ex: une fonction sqrt qui se trouve dans un module(Page) qui sapelle
    declaration:
        import [NomModule]
    utilisation:
        NomModule.fct()
si le nom dune fonction se trouve dans le module et dans mon code il n y aura 
pas de conflit car la donction du module serea dans lespoace de nom du module
un espace de nom est un espace memoire ou sont stocke des variables object fonction 

on peut changer lespace de nom du module
    ex: import math as mathematique
on peut importer qune fonction dun module 
    ex: from [NomModule] import [NomFonction]
        NomFonction()
        from [NomModule] import * ==> importe toutes lesfonction du module
                                      attention ces donction ne feront pas parti de l espace de nom du module risque de conflit
on peut importer un module a partir de linterpreteur python lui meme
    ex: import math 
on peut creer et importer ses propres module(un module est un fichier)
    ex: import [NomModule]
sous linux chaque fichier doit avoir comme premiere ligne 
 #!PathPython interpreteur
pour documenter un module ont met des docstring au debut du module

if __name__ == "__main__":
    permet d executer ce qui se trouve dans le if si laa page est executer non pas en taqnt que module mais en tant que fichier main
__name__ est une metavariable qui contient linformation si le fichier a son execution est le fichier executer en tant que main ou non

'''
#execution fichier py
'''
sous linux chaque fichier doit avoir comme premiere ligne 
 #!PathPython interpreteur
pour gerer lencodage juste apres on doit avoir 
windows  :# -*-coding:Latin-1 -*
linux    :# -*-coding:utf-8 -*
pour faire que lexecution se met en pause a la fin sous windows
    import os # On importe le module os qui dispose de variables 
              # et de fonctions utiles pour dialoguer avec votre 
              # système d'exploitation
    os.system("pause")
pour faire que lexecution se met en pause a la fin sous linux
    executer le programme dans la console ou mettre un input a la fin du fichier
'''

#Package
'''
un package est un  dossier dans lequel on regrouype un ou plusieur module ou package 
certain package ont un fichier __init__
    declaration:
        from [NomPackage].[NomModule] import [NomFonction]
        import [NomPackage].[NomModule] 
    utilisation:
        NomFonction()
        [NomPackage].[NomModule].NomFonction()

'''
