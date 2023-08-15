class Player:
    players=[]
    def __init__(self, username):
        self._username = username
        type(self).players.append(username)
       

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if isinstance(new_username, str) and 2<= len(new_username) <=16:
            self._username = new_username
        else:
            return print(f"username doesn't work")

    def results(self):
        new_list=[]
        for obj in Result.results:
            if obj.player == self:
                new_list.append(obj)
        return new_list

    def games_played(self):
        new_list=[]
        for obj in Result.results:
            if obj.player == self:
                new_list.append(obj.game)
        return list(set(new_list))

    def played_game(self, game):
        games_played=[]

        for obj in Result.results:
            if obj.game == game and obj.player == self:
                games_played.append(obj.game)
        return game in games_played


    def num_times_played(self, game):
        times_played = 0
        for obj in Result.results:
            if obj.game == game and obj.player == self:
                times_played += 1
        return times_played


from classes.result import Result
