import asteroid as a

class Score():
    def __init__(self):
        self.__score = 0
        self.__player_life = 3
    
    def get_score(self):
        return self.__score
    
    def add_score(self, score):
        self.__score += score
    
    def get_player_life(self):
        return self.__player_life

    def lose_life(self):
        self.__player_life -= 1