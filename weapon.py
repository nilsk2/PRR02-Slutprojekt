class Weapon: 
    def __init__(self, baseDmg, difficulty, weaponType): 
        self.__baseDmg = baseDmg
        self.__difficulty = difficulty
        self.__weaponType = weaponType
    
    @property
    def baseDmg(self):
        return self.__baseDmg
        
    @property
    def difficulty(self):
        return self.__difficulty
    
    @property
    def weaponType(self):
        selectWeapon(self)
        return self.__weaponType
    
    @staticmethod
    def selectWeapon(self):
        if weaponType == 1:
            SwordAndShield(self, 1.5, 1)

class SwordAndShield(Weapon):
    def __init__(self, defenseMult, damageMult, criticalHit):
        self.__defenseMult = defenseMult
        self.__damageMult = damageMult
        self.__criticalHit = criticalHit

    @property
    def defenseMult(self):
        return self.__defenseMult
    
    @property
    def damageMult(self):
        return self.__damageMult
    
    @property
    def criticalHit(self):
        return self.__criticalHit
