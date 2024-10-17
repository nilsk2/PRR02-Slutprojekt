roles = ["Warrior", "Mage", "Rogue", "Paladin", "Ranger"]

class weapon: 
    def __init__(self, weapon, base_dmg, difficulty): 
        print(weapon, base_dmg, difficulty) 
  
class character:
    def __init__(self, name, hp, weapon_name):
        self.name = name
        self.hp = hp
        self.obj1 = weapon(weapon_name, 20, 50)