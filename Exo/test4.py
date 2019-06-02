from Tools.Input import *


print('bonjour!! \n ceci est un programme pour savoir si une annee est bissextile ou non ')

year=inputInt('Votre year:')
print('solution prof:\t')
if year%400==0 or (year%4==0 and year%100!=0):
    print('l\'anne %r est bissextile\n'%year)
else:
    print('l\'anne %r n\'est pas bissextile\n'%year)

try:
    vara=int('k')

except ValueError as ErrRet:
    print('ValueError',ErrRet)
except TypeError:
    print('TypeError')
finally:
    print('We go throught a try')

try:
    vara=0
    assert vara > 0
except AssertionError as ErrRet:
    print('AssertionError1')
varb=1
try:
    assert varb==1
    varb=0
except AssertionError as ErrRet:
    print('AssertionError2')
try:
    varc=inputInt()
    if varc==4:
        assert varc ==4
except:
    pass
finally:
    varc=1
try:
    varc=inputInt()
    if varc==0:
        raise ValueError('int==0') 
except ValueError as ErrRet:
    print(ErrRet)

