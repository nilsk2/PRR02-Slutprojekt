from character import Character as char
import random as rand

adjective = ["The Great", "The Evil", "The Furious",
             "The Wicked", "The Vengeful", "The Dark",
             "The Cruel", "The Terrible", "The Mighty", "The Cursed"]

races = ["Dragon", "Behemoth", "Wraith",
         "Kraken", "Lich", "Gorgon",
         "Hydra", "Banshee", "Leviathan", "Minotaur"]

weapons = ["sword", "axe", "bow",
           "dagger", "spear", "crossbow",
           "mace", "hammer"]

####metoder

def ReadInt(message, min, max):
    while True:
        userInput = input(message).lower()
        try:
            userInput = int(userInput)
            if userInput < min or userInput > max:
                raise
            return userInput
        except:
            print(f"Invalid input! Must be a whole number in the range {min}-{max}")
            continue

##########

for item in weapons:
    print(f'{weapons.index(item)+1} {item}')
    
playerWeapon = weapons[(ReadInt("Choose your weapon: ", 0, 8))-1]

playerWeaponDamage = ReadInt("tune your weapon with 100 points, more damage = less accuracy: ", 0, 100)
plr = char("nils", 100, playerWeapon, playerWeaponDamage)

foeName = f'{rand.choice(adjective)} {rand.choice(races)}'
foe = char(foeName, 100, rand.choice(weapons), rand.randint(10, 90))

plr.Attack(foe)

#klasser:
#klass
#attacker
#vapen
#char
#mer
#fkdkfdk