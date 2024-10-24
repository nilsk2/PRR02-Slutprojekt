import random as rand

class Weapon: 
    def __init__(self, weapon, baseDmg, difficulty): 
        self.weapon = weapon
        self.baseDmg = baseDmg
        self.difficulty = difficulty
  
class Character:
    def __init__(self, name, hp, weaponName, weaponDamage):
        self.name = name
        self.hp = hp
        self.charWeapon = Weapon(weaponName, weaponDamage, 100-weaponDamage)

    def Attack(self, target):
        damage = self.charWeapon.baseDmg

        if rand.randrange(0,100) < self.charWeapon.difficulty:
            target.TakeDamage(damage)
        else:
            print("Miss!")
            target.TakeDamage(0)

    def TakeDamage(self, damage):
        self.hp -= damage
        if self.hp < 0: self.hp = 0
