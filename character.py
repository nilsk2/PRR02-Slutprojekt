class weapon: 
    def __init__(self, weapon, base_dmg, difficulty): 
        print(weapon, base_dmg, difficulty) 
  
class character:
    def __init__(self, name, hp, weaponName, weaponDamage):
        self.name = name
        self.hp = hp
        self.obj1 = weapon(weaponName, weaponDamage, 100-weaponDamage)