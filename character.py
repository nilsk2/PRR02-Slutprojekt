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
        # crits, buffs
        target.TakeDamage(damage)

    def TakeDamage(self, damage):
        self.hp -= damage
        if self.hp < 0: self.hp = 0
        print(self.name, self.hp)
