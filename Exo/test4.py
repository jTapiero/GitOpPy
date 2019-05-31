from Tools.Input import *


print('bonjour!! \n ceci est un programme pour savoir si une annee est bissextile ou non ')

year=inputInt('Votre year:')
print('solution prof:\t')
if year%400==0 or (year%4==0 and year%100!=0):
    print('l\'anne %r est bissextile\n'%year)
else:
    print('l\'anne %r n\'est pas bissextile\n'%year)
