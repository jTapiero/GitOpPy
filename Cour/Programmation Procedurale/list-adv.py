# List and String
'''
String to list
    string.split('') ==> separe une chaine de charactere en liste en prenant le parametre en tant que separateur
                         par defaut le parametre est espace tab et saut de ligne 
    ex:
        'string to str ing'.split() ==> ['string','to','str','ing']

list to string 

    "".join(list) ==> mais tous les elements de la liste dans une chaine separer par un espace 
    ex:
        "".join(['string','to','str','ing'])==> 'string to str ing'
        
'''
#List comprehension
'''
equivalent d une fonction lambda pour les listes
permettent de modifier tres rapidement une liste 
declaration:
    [(operation) for var in liste]
    [(operation) for var in liste if(predicat)]
utilisation:
    liste=[4,4,6,8,7]
    [nb*nb for nb in liste]             ==>[16,16,36,64,49]
    [nb for nb in liste if nb % 2 == 0] ==>[4,4,6,8]


'''
#
#
