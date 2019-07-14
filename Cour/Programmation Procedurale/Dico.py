#Dictionaire 
'''
contrairement au liste un dictionnaire peut contenir des objets
les dictionnaire marche selon une logique key-value
pour rajouter un element on le declare directement dans le dico
tous type peut servire de key meme des tuple
    ex:dec['h',1]='cavalier'
on peut mettre des fonctions dans un dictionnaire 
    ex: def fct .....
        dic[key]=fct
        utilisation:
            dic[key]()
declaration:
    dict()
    mon_dictionnaire = {}
    dic={'Key1': 'Value', 'Key2': 'Value2'}
    dic[Key3]=Value3

Utilisation:
    dic[Key1]=Value
    dic[Key1] ==> Value

fonction:
    del dic[Key] permet de suprimer un element du dico ou le dico si il n 'y a pas de parenthese apres
        ex: del dic[Key2]  ==> {'Key1': 'Value'}
    dic.pop(Key) permet d enlever l element et le renvoie  
        ex: dic.pop(Key1) ==> Value,{}

'''

#set
'''
un set est un ensemble delement dont aucun ne se resemble
declaration:
    set = {'value1', value2}

Utilisation:
'''