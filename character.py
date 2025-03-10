import random as rand
from weapon import Weapon
from stats import Stats
  
class Character:
    def __init__(self, name, hp, defense, weaponDamage, weaponType):
        self.__name = name
        self.__hp = hp
        self.__defense = defense
        self.__charWeapon = Weapon(weaponDamage, 100-weaponDamage, weaponType)

    def attack(self, target, my_stats, enemy_stats):
        damage = self.charWeapon.baseDmg
        randomValue = rand.randrange(0, 100)
        if randomValue < 10: 
            my_stats.criticalHits + 1
            my_stats.hits + 1
            print("Critical hit!")
            print(f"{damage * 1.5:.2f} damage is dealt by {self.name}")
            target.takeDamage(damage * 2, enemy_stats)
            return my_stats, enemy_stats
        elif randomValue < self.charWeapon.difficulty:
            my_stats.hits + 1
            print(f"{damage:.2f} damage is dealt by {self.name}")
            target.takeDamage(damage, enemy_stats)
            return my_stats, enemy_stats
            
        else:
            my_stats.misses + 1
            print(f"{self.name}'s attack misses")
            return my_stats, enemy_stats

    def takeDamage(self, damage, enemy_stats):
        enemy_stats.damage_taken + 1
        reducedDamage = max(0, damage * self.__defense)
        self.hp -= reducedDamage
        print(f'but {(damage - reducedDamage):.2f} damage is blocked!')
        print(f'Total damage taken: {reducedDamage:.2f}')

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
        print(self.__stats)
        return self.__stats