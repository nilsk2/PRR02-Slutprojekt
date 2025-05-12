from weapon import Weapon
# filen för wizardstaff vapnet, all info om vapnet sparas och tas här ifrån
class WizardStaff(Weapon):
    def __init__(self, defense_mult, damage_mult):
        self.__defense_mult = defense_mult
        self.__damage_mult = damage_mult
        
    @property
    def defense_mult(self):
        return 0.7
    
    @property
    def damage_mult(self):
        return 1.3
