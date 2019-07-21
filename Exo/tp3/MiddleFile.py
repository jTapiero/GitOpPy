""" Module permettant de gerer les enregistrement fichier"""
import os
import pickle

class MiddleFile:
    def __init__(self):
        self.pathData='./Exo/tp3/Donne'
        self.pathRoot=os.getcwd()
        self.fileData='player.txt'
    def initPath(self):
        os.chdir('./Exo/tp3/Donne')
    def goToRoot(self):
        os.chdir(self.pathRoot)
    def getAll(self):
        self.initPath()
        with open(self.fileData,'rb') as scoreFile:
            picklerObj=pickle.Unpickler(scoreFile)
            ListElem=list()
            while True :
                try:
                    ListElem.append(picklerObj.load())
                except:
                    break
        self.goToRoot()
        return ListElem
    
    def addPlayer(self, player):
        self.initPath()
        with open(self.fileData,'ab') as scoreFile:
            picklerObj=pickle.Pickler(scoreFile)
            picklerObj.dump(player)
        self.goToRoot()
        print('player ajoute')
    def isInDataBase(self, NamePlayer):
        dataBase=self.getAll()
        rslt=False
        if dataBase:
            for elem in dataBase:
                if elem['name'] == NamePlayer:
                    rslt=True
        return rslt
    def getPlayer(self, NamePlayer):
        dataBase=self.getAll()
        for elem in dataBase:
            if elem['name'] == NamePlayer:
                aPlayer=elem
        return aPlayer
    def updatePlayer(self, player):
        if self.isInDataBase(player['name']):
            dataBase=self.getAll()
            for elem in dataBase:
                if elem['name'] == player['name']:
                    elem['score']=player['score']
            self.initPath()
            with open(self.fileData,'wb') as scoreFile:
                picklerObj=pickle.Pickler(scoreFile)
                for elem in dataBase:
                    picklerObj.dump(elem)
            self.goToRoot()
            print('database updater')
    def printAllScore(self):
        nSize=0
        sSize=0
        for elem in self.getAll():
            nSize=max(nSize,len(elem['name']))
            sSize=max(sSize,len(str(elem['score'])))      
        nSize=max(nSize,len('name'))
        sSize=max(sSize,len('score'))
        print('_'*(nSize+sSize+7))
        print('|','name'.center(nSize),'|','score'.center(sSize),'|')
        print('|','_'*nSize,'|','_'*sSize,'|')
        for elem in self.getAll():
            print('|',str(elem['name']).center(nSize),'|',str(elem['score']).center(sSize),'|')
        print('|','_'*(nSize+sSize+3),'|')

       
