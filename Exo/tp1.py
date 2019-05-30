# -*-coding:Latin-1 -*

import os # On importe le module os qui dispose de variables 
          # et de fonctions utiles pour dialoguer avec votre 
          # système d'exploitation
#bissextile year

print('bonjour!! \n ceci est un programme pour savoir si une annee est bissextile ou non ')

year=int(input('Votre year:\n'))

print('solution 1:\t')
if year%4==0:
    print('l\'anne %r est bissextile\n'%year)
else:
    print('l\'anne %r n\'est pas bissextile\n'%year)

print('solution 2:\t')
if year%4==0:
    if year%100==0:
        if year%400==0:
            print('l\'anne %r est bissextile\n'%year)
        else:
            print('l\'anne %r n\'est pas bissextile\n'%year)
    else:
        print('l\'anne %r est bissextile\n'%year)
else:
    print('l\'anne %r n\'est pas bissextile\n'%year)

print('solution 3:\t')
if (year%4==0 or year%400==0) and year%100!=0:
    print('l\'anne %r est bissextile\n'%year)
else:
    print('l\'anne %r n\'est pas bissextile\n'%year)

print('solution 4:\t')
if year%400==0:
    print('l\'anne %r est bissextile\n'%year)
else:
    if year%100==0:
        print('l\'anne %r n\'est pas bissextile\n'%year) 
    elif year%4==0:
        print('l\'anne %r est bissextile\n'%year)
    else:
        print('l\'anne %r n\'est pas bissextile\n'%year)

print('solution prof:\t')
if year%400==0 or (year%4==0 and year%100!=0):
    print('l\'anne %r est bissextile\n'%year)
else:
    print('l\'anne %r n\'est pas bissextile\n'%year)

print('la solution 3 est defectueuse car si year ==400 il rentra en contradiction avec year non multiple de 100')

os.system("pause")