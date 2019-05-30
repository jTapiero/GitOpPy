#Operateur de comparaison et predicat
    '''
    chaque condition se fait par l intermediaiure d un predicat 
    qui selon son operateur de comparaison va renvoyer True or false 
    ex: 5 > 3 ==> True
        5 < 3 ==> False
    on peut gerer lordre des operateurs avec des parenthese 

    
    >    : strictement superieur 
    <   : strictement inferieur
    ==  : strictement egaux valeur
    === : strictement egaux valeur et type 
    >=  : superieur ou egal 
    <=  : inferieur ou egal
    !=  : different 
    and : les deux predicat doivent etre vrai  
    or  : l um des deux predicat doivent etre vrai 
    not : l inverse du predicat doit etre vrai
        ex:  not 5 < 3 ==> True
    is  :
        ex: if [predicat/valeur] is  not true 
        equivalent de ==
    in  : permet de verifier si un element se trouve dans un autre
        ex: if [valeur] in [liste] ==> renvoie true
        
    '''

#if-else-elif
    '''
    en python tout ce qui se trouve endenter
    au dessous dune commande est pour signifier que cest le contenu de la commande 
    if   :verifie si le predicat est vrai 
    else :cas ou le predicat est faux
    elif :cas ou le predicat est faux et on rajoute un predicat 
    on peut imbrique les if et on peut mettre autant d elif qu on veut
    on peut mettre plusieur predicat grace a and or not  


    declaration:
        1:  if [predicat]:
                cmd1         #si predicat == True
                cmd2 

        2:  if [predicat]:
                cmd1         #si predicat == True
                cmd2 
            else:
                cmd1         #si predicat == False
                cmd2
        
        3:  if [predicat]:
                cmd1         #si predicat == True
                cmd2 
            elif [predicat]:
                cmd1         #si predicat == False et on  rajoute un predicat pour des resultat affine
                cmd2
            else:
                cmd1         #si predicat == False
                cmd2

        4:  if [predicat]:
                cmd1         #si predicat == True
                cmd2 
            elif [predicat]:
                cmd1         #si predicat == False et on  rajoute un predicat pour des resultat affine

        5:  if [predicat]:
                if [predicat]:
                    cmd
                else:
                    cmd
            elif [predicat]:
                cmd
            elif [predicat]:
                if [predicat]:
                    cmd
                elif [predicat]:
                    cmd
                else:
                cmd        
            else:
                cmd    
        
        
    '''
