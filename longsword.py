from weapon import Weapon

class Longsword(Weapon):
    def __init__(self, defense_mult, damage_mult):
        self.__defense_mult = defense_mult
        self.__damage_mult = damage_mult
        
    @property
    def defense_mult(self):
        return self.__defense_mult
    
    @property
    def damage_mult(self):
        return self.__damage_mult
