# Fonction 
'''
une fonction est une suite d operatiomn qu on cherche a appeler plusieur fois dans notre code
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
#