#!/usr/bin/python3.6
''' Vigener Cypher Module '''
from Tools.Input import *

alph=['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
      'o','p','q','r','s','t','u','v','w','x','y','z']

def VigenerCypher(key,texte):
    '''
    crypte the message in fonction of the key\n
    key Str message to crypt the message \n
    texte Str message\n
    return crypted message 
    '''
    rslt=[]
    for idx,letter in enumerate(texte):
            if letter in alph:
                idxKey=idx%len(key)
                val1,val2=alph.index(letter),alph.index(key[idxKey])
                idxnewLet=(val1 + val2)%26
                rslt.append(alph[idxnewLet])
            else:
                rslt.append(letter)
    return ''.join(rslt)

def ReverseVigenerCypher(key,texte):
    '''decrypte the message in fonction of the key\n
    key Str message to decrypt the message \n
    texte Str message\n
    return uncrypted message'''
    rslt=[] 
    for idx,letter in enumerate(texte):
        if letter in alph:
            idxKey=idx%len(key)
            val1,val2=alph.index(letter),alph.index(key[idxKey])
            idxOldLet=(val1-val2)%26
            rslt.append(alph[idxOldLet])
        else:
            rslt.append(letter)

    return ''.join(rslt)

    

if __name__ == "__main__":
    print('Welcome to the vigener encryption module')
    while True:
        chx=inputInt('What do you do?:\n\t1)Crypt\n\t2)Decrypt\n\t3)Hard Decrypt\n\t4)Quit')
        if chx==1:
            texte=inputString('Enter the texte to crypte')
            key=inputString('give your key')
            Cypher=VigenerCypher(key,texte)
            print(Cypher)
        elif chx==2:
            texte=inputString('Enter the texte to decode')
            key=inputString('give your key')
            unCypher=ReverseVigenerCypher(key,texte)
            print(unCypher)
        elif chx==3:
            print('Nothing here yet')

        elif chx==4:
            break