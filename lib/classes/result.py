import ipdb
class Result:
    results=[]
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self._score = score
        type(self).results.append(self)
        
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, new_score):
        if isinstance(new_score, int) and 1<=new_score<5000:
            self._score=new_score
        else:
            print('something wrong with the score')

    # @property
    # def player(self):
    #     return self.player

    # @player.setter
    # def player(self, new_player):
    #     self.player= new_player

    # @property
    # def game(self):
    #     return self.game
    
    # @game.setter
    # def game(self, new_game):
    #     self.game= new_game
    def all(self):
        return len(results)


from classes.game import Game
from classes.player import Player

