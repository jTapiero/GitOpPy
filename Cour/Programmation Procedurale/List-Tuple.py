#List 
'''
une liste est un element composer et regroupant dautre element
une liste peut contenir une autre liste ,
elle peut aussi contenir des objets
les elements qui la composent ne sont pas toujours du meme type
chaque liste possedent un index corespondant a la position de l element dans la liste
    l index commence a 0
les listes sont mutable et modifiable a souait


declaration:
    Builder object : list() ==> list1=list()
                        list1 == >[]
    variable instantiation : list2=[],list3=[4,f,3.2]
                        list2 ==> []
                        list3 ==> [4,f,3.2]
                      
Utilisation:
    list1=[4,5,'g','h',[9,8]]
    list1[0] ==> 4
    list1[3] ==> 'h'
    list1[5] ==> [9,8]
    list1[5][1] ==> 8
    list1[0]=305 ==> [305,5,'g','h',[9,8]]

fonction:
list=[4,5,'g']
    list.append(x)  Permet de rajouter x a la fin de la liste (modifie la liste ne renvoie pas de resultat)
        ex: list.append(35) ==> [4,5,'g',35]
    list.insert(ind,x) permet d inserer x a la position numero 2(decale tout les elements)
        ex: list.insert(2,35) ==> [4,5,35,'g',35]
list2=[23.5,'yo',65]
    list.extend(list2) permet de rajouter a la fin de list list2
        ex: list.extend(list2) ==> [4,5,35,'g',35,23.5,'yo',65]
            ou list=list+list2 ==> [4,5,35,'g',35,23.5,'yo',65]
            ou list+=list2 ==> [4,5,35,'g',35,23.5,'yo',65]
    del list[ind] permet de suprimer un element de la liste ou la liste si il n'y a pas de crochet apres la variable
        ex: del list[0]  ==> [5,35,'g',35,23.5,'yo',65]
    list.remove(x) permet de retirer la premiere occurence de x se trouvant dans la list
        ex: list.remove(35)  ==> [5,'g',35,23.5,'yo',65]
    list.pop(inx) permet de suprimmer l element qui a l index inx 
        ex: list.pop(2)  ==> [5,'g',23.5,'yo',65]

    enumerate(list) permet de renvoyer un list composer de duet composer de l index et de son element associer [(0,x),(1,y)]
        ex: for i,elt in enumerate (list) 
                print(elt,i)  ==> x,0
                                  y,1
                                  ...

'''

#Tuple
'''
un tuple est comme une liste a lexeception pres que son contenue est immuable ou inchanchable
on ne peut le modifier apres sa declaration 
si on veut creer un tuple avec un seul et unique element on doit quand meme rajouter une virgule
les tuple sont sous entendu dans le cas de gestion de plusieurs variables tel que a,b=3,4

declaration:
    tuple=()
    tuple=(1,)
    tuple=(1,2,3)

Utilisation:
''' 
# Parcour des chaines ou liste  par indices 
'''
[0]  ==> premier element
[1]  ==> deuxieme element
...
[-1]  ==> derniere lettre de la chaine de charactere
[0][5] ==> cinquieme element s une liste qui se trouve etre le premier elements d une autre liste 
[]()  ==> appele d une fonction qui de trouve dans une liste  

ex while:
    i = 0 
    while i < len(chaine):
        print(chaine[i]) 
        i += 1

liste[0:2] du premier element inclus au troisieme exclu
liste[:2] du debut jusqu'au troisieme exclu
liste[2:] du troisieme element jusqu'a la fin  


''' 

