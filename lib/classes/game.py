import ipdb
class Game:
    def __init__(self, title):
        self._title = title
       
    @property   
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and len(new_title)>0:
            self._title= new_title
        else:
            print('Title not a string')
    
    def results(self):
        new_list=[]
        for obj in Result.results:
            if obj.game == self:
                new_list.append(obj)
        return new_list


    def players(self):
        new_list=[]
        for obj in Result.results:
            if obj.game == self:
                new_list.append(obj.player)
        return list(set(new_list))
        

    def average_score(self, player):
        average = 0
        division = 0
        for obj in Result.results:
            if obj.player == player:
                print(obj.score)
                average += obj.score
                division += 1
        return average/division
            
        



from classes.result import Result
from classes.player import Player

