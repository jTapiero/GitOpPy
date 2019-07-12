#os Package 
'''
le package os est un package qui permet de dialoguer avec l'OS de la machine 
permettant ainsi d acceder au fonctionnalite os,driver,software,hardware 

fct:
os.chdir('Path') ==> Change directory
    ==> Path str chemin relatif et/ou absolue 
os.getcwd() ==> return notre position dans le systeme de fichier 

'''
#Chemin relatif et absolue 
'''
chemin absolue:
    chemin qui decrit la position du fichier depuis la racine
        ex:/home/user/document/test.txt 
chemin relatif:
    chemin qui decrit la position du fichier par rapport a la position de l interpreteur 
    ../ represente le fichier parent 
        ex:../../doc/test.txt
'''
#File
'''
Open:
    fct open('file','Mode ouverture')
    Mode Ouverture:- r (read)        :lecture seule 
                - w (Write)       :ecriture depuis le haut du fichier (if not file then touch) 
                - a (Append)      :ecriture depuis la fin du fichier  (if not file then touch)
            (faclt)- b (binnary mode):associable aux trois autre permet douvrire en mode binaire 
    return un objet contenant le fichier 
    exemple:
    file=open('test.txt','a') ==> permet d ouvrire un fichier 
    file.read()               ==> renvoie une chaine de charactere qui contient le contenu du fichier    
    file.write("value")       ==> permet d ecrire une string contenant value dans le fichier renvoie le nombre de charactere ecrit 
    file.close()              ==> permet de fermer un fichier return true si le fichier est deja fermee

With
    permet de creer un bloc d instruction dans lequel on va faire nos operation sur nos fichier 
    ce bloc va automatiquement fermer le fichier qui a etais ouvert 
    ex:
        with open(mon_fichier, mode_ouverture) as variable:
            variable.read()   



'''  
#pickle Package 
'''
le package pickle est un package permettant de stocker un objet dans un fichier
il possede :- l'objet  pickler qui enregistre dans le fichier 
            - l'objet  unpicler qui sort les donne du fichier 
ouverture du fichier en mode binaire obligatoire 
'''
    #Pickler
    '''
    import pickle
    score = {"joueur 1": 5}
    with open('donnees', 'wb') as fichier:
        mon_pickler = pickle.Pickler(fichier) ==>objet pickle qui est construit a partir de l objet fichier
        mon_pickler.dump(score) permet d ecrire l objet sur le fichier 
    '''
    #UnPickler   
    '''
    import pickle
    with open('donnees', 'rb') as fichier:
        mon_depickler = pickle.Unpickler(fichier)
        donne = mon_depickler.load()==> permet de recuperer un objet et met le pointeur sur l objet suivant (doit etre appeler plusieur fois pour recuperer tous les objets)
        

    '''