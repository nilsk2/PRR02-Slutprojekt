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
    def __init__(self, name, hp, weaponDamage):
        self.__name = name
        self.__hp = hp
        self.__charWeapon = Weapon(weaponDamage, 100-weaponDamage)

    def attack(self, target): #fixa 
        damage = self.charWeapon.baseDmg
        randomValue = rand.randrange(0,100)
        if randomValue < 10: 
            target.takeDamage(damage*2)
            print("Critical hit!")
            print(f"{damage*2} damage is delt by {self.name}")
        elif randomValue < self.charWeapon.difficulty:
            target.takeDamage(damage)
            print(f"{damage} damage is delt by {self.name}")
        else:
            target.takeDamage(0)
            print(f"{self.name}'s attack misses")

    def takeDamage(self, damage):
        self.hp -= damage
        if self.hp < 0: self.hp = 0

    @property
    def name(self):
        return self.__name

    @property
    def hp(self):
        return self.__hp
    
    @property
    def charWeapon(self):
        return self.__charWeapon