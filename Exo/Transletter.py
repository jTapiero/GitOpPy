#!/bin/python
"""133t Translator Module"""
from Tools.Input import *

def i33tTrsl(texte):
    """
    133t Translator Fonction
    input(Param) ==> string
    ouput       ==> string  
    """
    output=[]
    dico={'a':'4',
          'o':'0',
          'e':'3',
          'i':'1',
          'w':'\\/\\/',
          'u':'|_|',
          's':'$',
          't':'7',
          'x':'*'}
    for letter in texte:
        if letter in dico.keys():
            output.append(dico[letter])
        else:
            output.append(letter)
    return ''.join(output)




if __name__ == "__main__": 
    texte=inputString('Rentrer texte:')
    ret=i33tTrsl(texte)
    print(ret)
