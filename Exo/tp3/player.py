class Player(object):
    def __init__(self):
        self.name=''
        self.point=8
        self.score=0
    def auth(self, player):
        self.name=player['name']
        self.score=player['score']
    def getDTPlayer(self):
        return {'name':self.name,'score':self.score}