import random as rand

class Weapon: 
    def __init__(self, baseDmg, difficulty): 
        self.baseDmg = baseDmg
        self.difficulty = difficulty
  
class Character:
    def __init__(self, name, hp, weaponDamage):
        self.name = name
        self.hp = hp
        self.charWeapon = Weapon(weaponDamage, 100-weaponDamage)

    def Attack(self, target):
        damage = self.charWeapon.baseDmg
        randomValue = rand.randrange(0,100)
        if randomValue < 10: 
            target.TakeDamage(damage*2)
            print("Critical hit!")
            print(f"{damage*2} damage is delt by {self.name}")
        elif randomValue < self.charWeapon.difficulty:
            target.TakeDamage(damage)
            print(f"{damage} damage is delt by {self.name}")
        else:
            target.TakeDamage(0)
            print(f"{self.name}'s attack misses")

    def TakeDamage(self, damage):
        self.hp -= damage
        if self.hp < 0: self.hp = 0
