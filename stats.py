class Stats:
    def __init__(self, weaponDamage):
        self.__hits = 0
        self.__damageGiven = 0
        self.__criticalHits = 0
        self.__baseDmg = weaponDamage
    
    @property
    def hits(self):
        return self.__hits

    @hits.setter
    def hits(self, value):
        self.__hits += value
    
