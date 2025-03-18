class Weapon: 
    def __init__(self, base_dmg, difficulty, weapon_type): 
        self.__base_dmg = base_dmg
        self.__difficulty = difficulty
        self.__weapon_type = weapon_type
        self.__custom = self.select_weapon(weapon_type)

    @property
    def base_dmg(self):
        return self.__base_dmg
        
    @property
    def difficulty(self):
        return self.__difficulty
    
    @property
    def weapon_type(self):
        self.select_weapon(self)
        return self.__weapon_type
    
    @staticmethod
    def select_weapon(weapon_type):
        from swordandshield import SwordAndShield
        from wizardstaff import WizardStaff
        from longsword import Longsword
        weapons = {
            1: SwordAndShield,
            2: WizardStaff,
            3: Longsword
        }
        player_weapon = weapons.get(weapon_type)(1, 2)
        print(player_weapon.defense_mult)
        return player_weapon
