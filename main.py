from character import character as char, weapon
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

for item in weapons:
    print(f'{weapons.index(item)+1} {item}')

while True:
    weapon_choice = input("Choose your weapon: ").lower().strip()
    try:
        index = int(weapon_choice)
        print(index)
        player_weapon = weapons[index-1]
        break
    except ValueError:
        if weapon_choice not in weapons:
            print("Invalid answer")
            continue
        player_weapon = weapons[weapons.index(weapon_choice)]
        break
    except IndexError:
        print("Invalid answer")
        continue

weapon_damage = input("tune your weapon with 100 points, more damage = less accuracy: ")

plr = char("nils", 100, player_weapon)

#foe saker
#foe_name = f'{rand.choice(adjective)} {rand.choice(races)}'
#print(foe_name)
#foe = char(foe_name, 100, weapon)

#klasser:
#klass
#attacker
#vapen
#char
#mer
#fkdkfdk