import random as rand

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
  
class Character:
    def __init__(self, name, hp, defense, weaponDamage):
        self.__name = name
        self.__hp = hp
        self.__defense = defense
        self.__charWeapon = Weapon(weaponDamage, 100-weaponDamage)

    def attack(self, target):
        damage = self.charWeapon.baseDmg
        randomValue = rand.randrange(0, 100)
        if randomValue < 10: 
            print("Critical hit!")
            print(f"{round(damage * 2, 2)} damage is dealt by {self.name}")
            target.takeDamage(damage * 2)
        elif randomValue < self.charWeapon.difficulty:
            print(f"{round(damage, 2)} damage is dealt by {self.name}")
            target.takeDamage(damage)
        else:
            print(f"{self.name}'s attack misses")
            target.takeDamage(0)

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
