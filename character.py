import random as rand
from weapon import Weapon
from stats import Stats
  
class Character:
    def __init__(self, name, hp, defense, weaponDamage, weaponType):
        self.__name = name
        self.__hp = hp
        self.__defense = defense
        self.__charWeapon = Weapon(weaponDamage, 100-weaponDamage, weaponType)
        self.__stats = Stats(weaponDamage)

    def attack(self, target):
        damage = self.charWeapon.baseDmg
        randomValue = rand.randrange(0, 100)
        if randomValue < 10: 
            print("Critical hit!")
            print(f"{round(damage * 1.5, 2)} damage is dealt by {self.name}")
            target.takeDamage(damage * 2)
            self.__stats.hits = self.__stats.hits + 1
        elif randomValue < self.charWeapon.difficulty:
            print(f"{round(damage, 2)} damage is dealt by {self.name}")
            target.takeDamage(damage)
            self.__stats.hits = self.__stats.hits + 1
            
        else:
            print(f"{self.name}'s attack misses")

    def takeDamage(self, damage):
        reducedDamage = max(0, round(damage * self.__defense, 2))
        self.hp -= reducedDamage
        print(f'but {round(damage - reducedDamage, 2)} damage is blocked!')
        print(f'Total damage taken: {reducedDamage}')

    @property
    def name(self):
        return self.__name

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if value < 0:
            self.__hp = 0
        else:
            self.__hp = value
    
    @property
    def defense(self):
        return self.__defense

    @property
    def charWeapon(self):
        return self.__charWeapon
    
    @property
    def stats(self):
        return self.__stats