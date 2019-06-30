#!/usr/bin/python3.6
''' Caesar Cypher Module '''
from Tools.Input import *

alph=['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
      'o','p','q','r','s','t','u','v','w','x','y','z']

def CaesarCypher(shift,texte):
    '''
    crypte the message in fonction of the shift\n
    shift int number to set off the alphabet \n
    texte Str message\n
    return crypted message 
    '''
    rslt=[]
    for letter in texte:
        if letter in alph:
            trs=(alph.index(letter)+(shift))%26
            rslt.append(alph[trs])
        else:
            rslt.append(letter)
    return ''.join(rslt)

def ReverseCaesarCypher(unShift,texte):
    '''decrypte the message in fonction of the shift\n
    unShift int number to set off the alphabet \n
    texte Str message\n
    return uncrypted message''' 
    rslt=[]
    for letter in texte:
        if letter in alph:
            trs=(alph.index(letter)-(unShift))%26
            rslt.append(alph[trs])
        else:
            rslt.append(letter)
    return ''.join(rslt)
def hardDecriptCeasarCypher(texte):
    rslts=[]
    i=0
    while i<25:
        rslt=ReverseCaesarCypher(i,texte)
        rslts.append(rslt)
        i+=1
    return rslts
    

if __name__ == "__main__":
    print('Welcome to the Ceasar encryption module')
    while True:
        chx=inputInt('What do you do?:\n\t1)Crypt\n\t2)Decrypt\n\t3)Hard Decrypt\n\t4)Quit')
        if chx==1:
            texte=inputString('Enter the texte to Code')
            shift=inputInt('give a offset number until from 1 to 26')
            Cypher=CaesarCypher(shift,texte)
            print(Cypher)
        elif chx==2:
            texte=inputString('Enter the texte to decode')
            unShift=inputInt('give a offset number until from 1 to 26')
            unCypher=ReverseCaesarCypher(unShift,texte)
            print(unCypher)
        elif chx==3:
            texte=inputString('Enter the texte to decode')
            rslts=hardDecriptCeasarCypher(texte)
            for indx,elt in enumerate(rslts):
                print('Mod {0}:\n\t{1}'.format(indx,elt))
        elif chx==4:
            break