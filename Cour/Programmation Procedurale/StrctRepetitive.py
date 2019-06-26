# While 
'''
    en python tout ce qui se trouve 
    en dessous + tab  dune commande est pour signifier que cest le contenu de la commande 
    while :s'exectute tant que le predicat est vrai   
    on peut imbrique les while comme on veut 
    on peut mettre plusieur predicat grace a and or not
    ne pas oublier un increment afin que le predicat devient faux sinon on risque une boucle infinie
      


    declaration:
        1:  while [predicat]:
                cmd1         
                cmd2 

'''
# for foreach
'''
    en python tout ce qui se trouve 
    en dessous+tabs dune commande est pour signifier que cest le contenu de la commande 
    for :s'exectute pour tout les elements dune sequence   
    on peut imbrique les for comme on veut 
    for est l'equivalent des foreach en python
    une chaine de charactere est une liste 


    declaration:
        for [NomVar:entitetableau] in [tableau/sequence/liste]:
            NomVar+1         
            cmd2 

'''
# in, break, continue
    #in
    '''
    peut s utiliser comme predicat pour verifier si un element peut se trouver dans un autre 
    ex: if [valeur] in [liste] ==> renvoie true

    '''
    #break
    '''
    break s utilise dans des while et for 
    il permet de quitter le boucle automatiquement 
    ex : while i<10:
            if i==2:
                break
            i+=1
        i sera egale a 2 a la fin du programme 
    '''
    #continue
    '''
    continue s utilise dans des while et for 
    il permet de revenir au debut du bloc d instruction sans pour autant 
    executer le reste de la boucle le boucle automatiquement 
    ex : while i<10:
            if i==2:
                i+=15
                continue
            i+=1
        i sera egale a 17 et non a 18 a la fin du programme car le continue a permis de sauter la derniere instruction
    '''