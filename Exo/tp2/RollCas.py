""" function associate to the rollGame  """
import Input ,math

def isColor (nb):
    """return a string the color of the number"""
    if nb%2!=0:
        return 'Red'
    if nb%2==0:
        return 'Black'
def putMise(arg):
    """get the mise and check if the mise is possible """
    try:
        mise=Input.inputInt('How many do you want to bet?')
        assert mise <= arg
        if mise<=0:
            raise ValueError('you can\'t bet 0 or less')
    except AssertionError as retErr:
        print('you can\'t bet more than you have {0}$'.format(arg))
        return putMise(arg)
    except ValueError as retErr:
        print(retErr)
        return putMise(arg)
    else:
        return mise

def putNumber():
    """get the Number and check if the num is possible """
    try:
        nbr=Input.inputInt('On which number?')
        assert nbr>=1 and nbr<=50 
    except AssertionError as retErr:
        print('The roll have only 50 entry')
        return putNumber()
    else:
        return nbr

def Rule ():
    """print the rule of the game """
    print('You begin with 500$ \n each turn you put a sum on a number between 1 and 50 incluse ')
    print('if the same number than you go out:\n\t-->you gain your mise and the triple of the sum')    
    print('if you have the same color than the number who go out:\n\t-->you gain  your mise and the half it')
    print('if you have no match :\n\t-->you lose your mise')
    print('you have 3000$:\n\t-->you win the gain \n you have 0$ or less:\n\t you lose the game')


def getGain(mise,VarA,nbr):
    """calcul the gain of the bet """
    gain=0
    if VarA==nbr:
        print('Jackpot you gain X3 the Bet')
        gain=mise*3
    elif VarA%2==nbr%2:
        print('Same Color You gain Half of the bet')
        gain=math.ceil(mise/2)
    else:
        print('Whoops you gain nothing')
        gain=-mise          
    return gain

