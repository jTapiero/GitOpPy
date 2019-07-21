import player,pendu,MiddleFile
from Input import *
import os 
def RuleGame():
    '''Affiche les regles du jeu '''
    print('jeu du pendu:')
    print('regle:\n\t-un mot est choisie au hasard dans une liste de mot de longueur max 8\n\t-Vs avez 8 vie ')
    print('\t-Chaque tour vous devez deviner une lettre du mot \n\t-si vous deviner une ou plusieurs lettres du mot les lettres apparaissent ')
    print('\t-sinon vous perdez une vie \n\t-vous deviner le mot: votre nombre de vie restant sajoute a votre score totale ')
    print('\t-vous le deviner pas vous avez perdu')
    os.system('pause')
    os.system('clear')
def run():
    RuleGame()
    thePlayer=player.Player()
    theMdf=MiddleFile.MiddleFile()
    
    name=inputString('quel est votre nom svp?')
    if theMdf.isInDataBase(name):
        print('welcome {0}'.format(name))
        thePlayer.auth(theMdf.getPlayer(name))
        print('vous avez un score actuel de  {0}'.format(thePlayer.score))
    else:
        print('welcome new Player {0}'.format(name))
        thePlayer.name=name
        theMdf.addPlayer(thePlayer.getDTPlayer())
    os.system('pause')
    os.system('clear')
    again=True
    while again:
        thePendu=pendu.Pendu()
        while thePlayer.point!=0:
            print(thePendu.getCipher())
            letter=thePendu.inputLetter('quelle est votre lettre ')
            if thePendu.checkLetter(letter):
                print('bravo tu as trouve la lettre {0}'.format(letter))
                thePendu.replaceCypher(letter)
            else:
                print('perdu ce n est pas la lettre {0}'.format(letter))
                thePlayer.point-=1
                print('il te reste {0} point de vie'.format(thePlayer.point))

            if thePendu.isAWin():
                print('felicitation le mot etais {0},Vous gagnez {1} point \n votre score est de {2}'.format(thePendu.mot,thePlayer.point,(thePlayer.score+thePlayer.point)))
                thePlayer.score+=thePlayer.point
                theMdf.updatePlayer(thePlayer.getDTPlayer())
                break
            if thePlayer.point==0:
                print('tu as perdu le mot etais {0},tu as {1} point \n ton score est de {2}'.format(thePendu.mot,thePlayer.point,(thePlayer.score+thePlayer.point)))
        os.system('pause')
        os.system('clear')
        print('ALL STAR TAB')
        print(theMdf.printAllScore())
        os.system('pause')
        os.system('clear')
        chois=input('voulez vous rejouer?(o)')
        if chois=='o':
            thePlayer.point=8
        else:
            print('Bye !!!')
            again=False

run()