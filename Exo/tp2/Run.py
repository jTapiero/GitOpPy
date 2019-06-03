"""
Tp open classroom Z casino 
"""
import random 
import Input ,RollCas

print('Welcome to Zcasino!!! \n here the Rule: ')
RollCas.Rule()

print('you begin the game!!')
arg=500
turn=1
while arg>0 and arg<3000 :
    print('Turn {0} : {1}$'.format(turn,arg))
    mise=RollCas.putMise(arg)
    nbr=RollCas.putNumber()
    varA=random.randint(1,50)
    print('The Roll roll and you get the {0} {1}'.format(varA,RollCas.isColor(varA)))
    gain=RollCas.getGain(mise,varA,nbr)
    arg+=gain
    turn+=1

if arg>=3000:
    print('Congratulation!!! You win the game with{0}$'.format(arg))
elif arg<=0:
    print('Whoops You lose the game with {0}$'.format(arg))

