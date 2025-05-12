from weapon import Weapon
# filen för sword and shield vapnet, all info om vapnet sparas och tas härifrån
class SwordAndShield(Weapon):
    def __init__(self, defense_mult, damage_mult):
        self.__defense_mult = defense_mult
        self.__damage_mult = damage_mult
        
    @property
    def defense_mult(self):
        return 1.2
    
    @property
    def damage_mult(self):
        return 0.9
