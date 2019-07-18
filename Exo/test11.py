import os
import pickle
yo=85
dico={'salut':456}
dico['yo']=35
for elem in dico.items():
    print(elem)


def getDico():
    """"""
    with open('joueur.txt','rb') as scoreFile:
        picklerObj=pickle.Unpickler(scoreFile)
        try:
            DicoScore=picklerObj.load()
        except:
            
            DicoScore={}
        return DicoScore



os.chdir('./Exo/tp3/Donne')

Score=getDico()
print(Score)
for key,value in Score.items():
    print(key,value)


