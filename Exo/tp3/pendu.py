import random
class Pendu:
    dico=["armoire","boucle","buisson","bureau","chaise","carton","couteau","fichier","garage","glace","journal","kiwi","lampe","liste","montagne","remise","sandale","taxi","vampire","volant"]
    alph=['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
      'o','p','q','r','s','t','u','v','w','x','y','z']
    def __init__(self):
        self.mot=self.dico[random.randint(0,19)]
        self.cipher=list()
        for letter in self.mot:
            self.cipher.append([letter,'*'])
    def getCipher(self):
        rslt=list()
        for elem in self.cipher:
            rslt.append(elem[1])
        return ''.join(rslt)
    def isInWord(self,letter):
        if letter in self.mot:
            return True
        else:
            return False
    def isAWin(self):
        if self.mot == self.getCipher():
            return True
        else:
            return False
    def checkLetter(self,letter):
        if letter in self.mot:
            return True
        else:
            return False
    def inputLetter(self,message):
        varString=input(message+" (Must be String Type+ alphabet character):")
        if varString in self.alph:
            return varString
        else:
            print(" A STRING ALPHABET CHARACTER")
            return self.inputLetter(message)
    def replaceCypher(self,letter):
        for elem in self.cipher:
            if letter == elem[0]:
                elem[1]=elem[0]






