#String 
'''
le type String de part sa complexite part sa complexite possede des caracteristiques plus nombreuse que les qutres types 
ses caracteristique et fonctioonalite suplementaire decoulent du fait qu il est plus considerer comme un objet

on ne peut pas modifier une element d une chaine


'''
    #Fonction 
    '''
    VarString.lower()      ==> transforme VarString en minuscule (renvoie la chaine en min mais ne le transforme pas)
    VarString.upper()      ==> transforme VarString en Majuscule (renvoie la chaine en min mais ne le transforme pas)
    VarString.capitalize() ==> transforme la premiere lettre de VarString en majuscule  (renvoie la chaine en min mais ne le transforme pas)
    VarString.strip()      ==> retire les espaces en debut et/ou en fin de chaine  (renvoie la chaine en min mais ne le transforme pas)
    VarString.fct.center(x) ==> apres application de fct permet de centrer la chaine dans une chaine de longueur x (rajoute des espaces)(renvoie la chaine en min mais ne le transforme pas)
    '''
    #Format
    '''
    Format permet de declarer une string qui aura des balises permettant d inserer de maniere automatique le contenu des variables 
    "string str strin {0} st {1} ,{2}".format(var1,var2,var3)
    0 represente la premire variable contenu dans format 
    1 represente la deuxieme var2
    2 represente la troisiueme var 3

    ex:
        "string {0} {1} ({3} {0} string ) string  {2} ".format(var1, var2, var3, var2.upper()))
    
    "string str strin {} st {} ,{}".format(var1,var2,var3) 
    si les nombre ne sont pas la c estl ordre de format qui compte 
    
    "string str strin {var1} st {var2} ,{var3}".format(var1=value,var2=value2,var3=value3)
    '''  
    # Concatenation des chaine 
    '''
    la concatenation des chaines est le fait d additioner deux chaine de charactere 

    utilisation:
    string=string1+string2
    string=string1+" "+string2
    string=string1+str(var)+string2

    modificatiobn des chaine de charactere:
        mot = "lac"
        mot = "b" + mot[1:]
        print(mot) ==> bac

        count   ??
        find    ??
        replace ??

    ''' 
