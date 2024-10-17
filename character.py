roles = ["Warrior", "Mage", "Rogue", "Paladin", "Ranger"]


class character:
    def __init__(self, name, hp, weapon):
        print("ok")
        self.name = name
        self.weapon = weapon()


class weapon:
    print("okgfs")