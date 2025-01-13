class Weapon: 
    def __init__(self, baseDmg, difficulty): 
        self.__baseDmg = baseDmg
        self.__difficulty = difficulty
    
    @property
    def baseDmg(self):
        return self.__baseDmg
        
    @property
    def difficulty(self):
        return self.__difficulty